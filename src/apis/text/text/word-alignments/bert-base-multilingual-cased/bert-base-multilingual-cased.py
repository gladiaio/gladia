import itertools

import torch
import transformers


def get_tokens(
    input_string: str, tokenizer: transformers.PreTrainedTokenizer
) -> ([str], [[str]]):
    """
    Tokenize an input string

    :param input_string: string to tokenize
    :param tokenizer: tokenizer to use
    :return: tuple contained the string splited by space and the tokenized string
    """

    sentence = input_string.strip().split()
    token = [tokenizer.tokenize(word) for word in sentence]

    return sentence, token


def tokens_to_tensor(
    tokens: [[str]], tokenizer: transformers.PreTrainedTokenizer
) -> torch.Tensor:
    """
    From a given tokenized sentence, return it as a Tensor

    :param tokens: tokens to transform
    :param tokenizer: tokenizer used to tokenize the text
    :return: tensor containing the tokens
    """

    ids = [tokenizer.convert_tokens_to_ids(t) for t in tokens]

    prepared_ids = tokenizer.prepare_for_model(
        ids=list(itertools.chain(*ids)),
        return_tensors="pt",
        model_max_length=tokenizer.model_max_length,
        truncation=True,
    )

    return prepared_ids["input_ids"]


def map_tokens_to_words(tokens: [[str]]) -> [int]:
    """
    Associate tokens to their respective words.

    :param tokens: tokens to associate to
    :return: word index for which the token come from
    """

    tok2word_map = []

    for i, word_list in enumerate(tokens):
        tok2word_map += [i] * len(word_list)

    return tok2word_map


def get_words_alignment(
    sentence_src: [str],
    sentence_tgt: [str],
    tok2word_map_src: [int],
    tok2word_map_tgt: [int],
    softmax_inter: torch.Tensor,
) -> [dict]:
    """
    Associate words from sentence_src to sentence_tgt

    :param sentence_src: splited source sentence
    :param sentence_tgt: splited target sentence
    :param tok2word_map_src: map associating tokens to their words for source sentence
    :param tok2word_map_tgt: map associating tokens to their words for target sentence
    :param softmax_inter: tell whether or to not add each word
    :return: word alignment from source to target
    """

    align_words = set()
    for i, j in torch.nonzero(softmax_inter, as_tuple=False):
        align_words.add((tok2word_map_src[i], tok2word_map_tgt[j]))

    output = []
    for i, j in sorted(align_words):
        output.append({"source": sentence_src[i], "target": sentence_tgt[j]})

    return output


def predict(input_string_language_1: str, input_string_language_2: str) -> [dict]:
    """
    Associated words from `input_string_language_1` to `input_string_language_2`.

    :param input_string_language_1: sentence to associate from
    :param input_string_language_2: sentence to associate to
    :return: list of dict associated each word from source to targe
    """

    threshold = 1e-3
    align_layer = 8
    model_name = "bert-base-multilingual-cased"

    model = transformers.BertModel.from_pretrained(model_name)
    tokenizer = transformers.BertTokenizer.from_pretrained(model_name)

    model.eval()

    sentence_src, tokens_src = get_tokens(input_string_language_1, tokenizer)
    sentence_tgt, tokens_tgt = get_tokens(input_string_language_2, tokenizer)

    tensor_src = tokens_to_tensor(tokens=tokens_src, tokenizer=tokenizer)
    tensor_tgt = tokens_to_tensor(tokens=tokens_tgt, tokenizer=tokenizer)

    tok2word_map_src = map_tokens_to_words(tokens_src)
    tok2word_map_tgt = map_tokens_to_words(tokens_tgt)

    with torch.no_grad():
        out_src = model(tensor_src.unsqueeze(0), output_hidden_states=True)[2][
            align_layer
        ][0, 1:-1]
        out_tgt = model(tensor_tgt.unsqueeze(0), output_hidden_states=True)[2][
            align_layer
        ][0, 1:-1]

    del tensor_src, tensor_tgt

    dot_prod = torch.matmul(out_src, out_tgt.transpose(-1, -2))

    softmax_inter = (torch.nn.Softmax(dim=-1)(dot_prod) > threshold) * (
        torch.nn.Softmax(dim=-2)(dot_prod) > threshold
    )

    return get_words_alignment(
        sentence_src=sentence_src,
        sentence_tgt=sentence_tgt,
        tok2word_map_src=tok2word_map_src,
        tok2word_map_tgt=tok2word_map_tgt,
        softmax_inter=softmax_inter,
    )
