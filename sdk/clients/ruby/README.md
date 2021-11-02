# openapi_client

OpenapiClient - the Ruby gem for the FastAPI

No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

This SDK is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 0.1.0
- Package version: 1.0.0
- Build package: org.openapitools.codegen.languages.RubyClientCodegen

## Installation

### Build a gem

To build the Ruby code into a gem:

```shell
gem build openapi_client.gemspec
```

Then either install the gem locally:

```shell
gem install ./openapi_client-1.0.0.gem
```

(for development, run `gem install --dev ./openapi_client-1.0.0.gem` to install the development dependencies)

or publish the gem to a gem hosting service, e.g. [RubyGems](https://rubygems.org/).

Finally add this to the Gemfile:

    gem 'openapi_client', '~> 1.0.0'

### Install from Git

If the Ruby gem is hosted at a git repository: https://github.com/GIT_USER_ID/GIT_REPO_ID, then add the following in the Gemfile:

    gem 'openapi_client', :git => 'https://github.com/GIT_USER_ID/GIT_REPO_ID.git'

### Include the Ruby code directly

Include the Ruby code directly using `-I` as follows:

```shell
ruby -Ilib script.rb
```

## Getting Started

Please follow the [installation](#installation) procedure and then run the following code:

```ruby
# Load the gem
require 'openapi_client'

api_instance = OpenapiClient::ImageImageBackgroundRemovalApi.new
image = File.new('/path/to/file') # File | 
opts = {
  model: 'rembg' # String | 
}

begin
  #Apply model for the background-removal task for a given models
  result = api_instance.apply_image_image_background_removal_post(image, opts)
  p result
rescue OpenapiClient::ApiError => e
  puts "Exception when calling ImageImageBackgroundRemovalApi->apply_image_image_background_removal_post: #{e}"
end

```

## Documentation for API Endpoints

All URIs are relative to *http://localhost*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*OpenapiClient::ImageImageBackgroundRemovalApi* | [**apply_image_image_background_removal_post**](docs/ImageImageBackgroundRemovalApi.md#apply_image_image_background_removal_post) | **POST** /image/image/background-removal/ | Apply model for the background-removal task for a given models
*OpenapiClient::ImageImageBackgroundRemovalApi* | [**get_versions_image_image_background_removal_get**](docs/ImageImageBackgroundRemovalApi.md#get_versions_image_image_background_removal_get) | **GET** /image/image/background-removal/ | Get list of models available for background-removal
*OpenapiClient::ImageImageColorizationApi* | [**apply_image_image_colorization_post**](docs/ImageImageColorizationApi.md#apply_image_image_colorization_post) | **POST** /image/image/colorization/ | Apply model for the colorization task for a given models
*OpenapiClient::ImageImageColorizationApi* | [**get_versions_image_image_colorization_get**](docs/ImageImageColorizationApi.md#get_versions_image_image_colorization_get) | **GET** /image/image/colorization/ | Get list of models available for colorization
*OpenapiClient::ImageImageFaceBluringApi* | [**apply_image_image_face_bluring_post**](docs/ImageImageFaceBluringApi.md#apply_image_image_face_bluring_post) | **POST** /image/image/face-bluring/ | Apply model for the face-bluring task for a given models
*OpenapiClient::ImageImageFaceBluringApi* | [**get_versions_image_image_face_bluring_get**](docs/ImageImageFaceBluringApi.md#get_versions_image_image_face_bluring_get) | **GET** /image/image/face-bluring/ | Get list of models available for face-bluring
*OpenapiClient::ImageImageRestorationApi* | [**apply_image_image_restoration_post**](docs/ImageImageRestorationApi.md#apply_image_image_restoration_post) | **POST** /image/image/restoration/ | Apply model for the restoration task for a given models
*OpenapiClient::ImageImageRestorationApi* | [**get_versions_image_image_restoration_get**](docs/ImageImageRestorationApi.md#get_versions_image_image_restoration_get) | **GET** /image/image/restoration/ | Get list of models available for restoration
*OpenapiClient::ImageImageSuperResolutionApi* | [**apply_image_image_super_resolution_post**](docs/ImageImageSuperResolutionApi.md#apply_image_image_super_resolution_post) | **POST** /image/image/super-resolution/ | Apply model for the super-resolution task for a given models
*OpenapiClient::ImageImageSuperResolutionApi* | [**get_versions_image_image_super_resolution_get**](docs/ImageImageSuperResolutionApi.md#get_versions_image_image_super_resolution_get) | **GET** /image/image/super-resolution/ | Get list of models available for super-resolution
*OpenapiClient::ImageImageUncolorizationApi* | [**apply_image_image_uncolorization_post**](docs/ImageImageUncolorizationApi.md#apply_image_image_uncolorization_post) | **POST** /image/image/uncolorization/ | Apply model for the uncolorization task for a given models
*OpenapiClient::ImageImageUncolorizationApi* | [**get_versions_image_image_uncolorization_get**](docs/ImageImageUncolorizationApi.md#get_versions_image_image_uncolorization_get) | **GET** /image/image/uncolorization/ | Get list of models available for uncolorization
*OpenapiClient::TextTextAutocorrectApi* | [**apply_text_text_autocorrect_post**](docs/TextTextAutocorrectApi.md#apply_text_text_autocorrect_post) | **POST** /text/text/autocorrect/ | Apply model for the autocorrect task for a given models
*OpenapiClient::TextTextAutocorrectApi* | [**get_versions_text_text_autocorrect_get**](docs/TextTextAutocorrectApi.md#get_versions_text_text_autocorrect_get) | **GET** /text/text/autocorrect/ | Get list of models available for autocorrect
*OpenapiClient::TextTextBooleanQuestionGenerationApi* | [**apply_text_text_boolean_question_generation_post**](docs/TextTextBooleanQuestionGenerationApi.md#apply_text_text_boolean_question_generation_post) | **POST** /text/text/boolean-question-generation/ | Apply model for the boolean-question-generation task for a given models
*OpenapiClient::TextTextBooleanQuestionGenerationApi* | [**get_versions_text_text_boolean_question_generation_get**](docs/TextTextBooleanQuestionGenerationApi.md#get_versions_text_text_boolean_question_generation_get) | **GET** /text/text/boolean-question-generation/ | Get list of models available for boolean-question-generation
*OpenapiClient::TextTextDependencyTrackingApi* | [**apply_text_text_dependency_tracking_post**](docs/TextTextDependencyTrackingApi.md#apply_text_text_dependency_tracking_post) | **POST** /text/text/dependency-tracking/ | Apply model for the dependency-tracking task for a given models
*OpenapiClient::TextTextDependencyTrackingApi* | [**get_versions_text_text_dependency_tracking_get**](docs/TextTextDependencyTrackingApi.md#get_versions_text_text_dependency_tracking_get) | **GET** /text/text/dependency-tracking/ | Get list of models available for dependency-tracking
*OpenapiClient::TextTextEmotionRecognitionApi* | [**apply_text_text_emotion_recognition_post**](docs/TextTextEmotionRecognitionApi.md#apply_text_text_emotion_recognition_post) | **POST** /text/text/emotion-recognition/ | Apply model for the emotion-recognition task for a given models
*OpenapiClient::TextTextEmotionRecognitionApi* | [**get_versions_text_text_emotion_recognition_get**](docs/TextTextEmotionRecognitionApi.md#get_versions_text_text_emotion_recognition_get) | **GET** /text/text/emotion-recognition/ | Get list of models available for emotion-recognition
*OpenapiClient::TextTextEntityExtractionApi* | [**apply_text_text_entity_extraction_post**](docs/TextTextEntityExtractionApi.md#apply_text_text_entity_extraction_post) | **POST** /text/text/entity-extraction/ | Apply model for the entity-extraction task for a given models
*OpenapiClient::TextTextEntityExtractionApi* | [**get_versions_text_text_entity_extraction_get**](docs/TextTextEntityExtractionApi.md#get_versions_text_text_entity_extraction_get) | **GET** /text/text/entity-extraction/ | Get list of models available for entity-extraction
*OpenapiClient::TextTextHateSpeechDetectionApi* | [**apply_text_text_hate_speech_detection_post**](docs/TextTextHateSpeechDetectionApi.md#apply_text_text_hate_speech_detection_post) | **POST** /text/text/hate-speech-detection/ | Apply model for the hate-speech-detection task for a given models
*OpenapiClient::TextTextHateSpeechDetectionApi* | [**get_versions_text_text_hate_speech_detection_get**](docs/TextTextHateSpeechDetectionApi.md#get_versions_text_text_hate_speech_detection_get) | **GET** /text/text/hate-speech-detection/ | Get list of models available for hate-speech-detection
*OpenapiClient::TextTextKeywordExtractionApi* | [**apply_text_text_keyword_extraction_post**](docs/TextTextKeywordExtractionApi.md#apply_text_text_keyword_extraction_post) | **POST** /text/text/keyword-extraction/ | Apply model for the keyword-extraction task for a given models
*OpenapiClient::TextTextKeywordExtractionApi* | [**get_versions_text_text_keyword_extraction_get**](docs/TextTextKeywordExtractionApi.md#get_versions_text_text_keyword_extraction_get) | **GET** /text/text/keyword-extraction/ | Get list of models available for keyword-extraction
*OpenapiClient::TextTextLanguageDetectionApi* | [**apply_text_text_language_detection_post**](docs/TextTextLanguageDetectionApi.md#apply_text_text_language_detection_post) | **POST** /text/text/language-detection/ | Apply model for the language-detection task for a given models
*OpenapiClient::TextTextLanguageDetectionApi* | [**get_versions_text_text_language_detection_get**](docs/TextTextLanguageDetectionApi.md#get_versions_text_text_language_detection_get) | **GET** /text/text/language-detection/ | Get list of models available for language-detection
*OpenapiClient::TextTextLanguageGenerationApi* | [**apply_text_text_language_generation_post**](docs/TextTextLanguageGenerationApi.md#apply_text_text_language_generation_post) | **POST** /text/text/language-generation/ | Apply model for the language-generation task for a given models
*OpenapiClient::TextTextLanguageGenerationApi* | [**get_versions_text_text_language_generation_get**](docs/TextTextLanguageGenerationApi.md#get_versions_text_text_language_generation_get) | **GET** /text/text/language-generation/ | Get list of models available for language-generation
*OpenapiClient::TextTextLemmatizationApi* | [**apply_text_text_lemmatization_post**](docs/TextTextLemmatizationApi.md#apply_text_text_lemmatization_post) | **POST** /text/text/lemmatization/ | Apply model for the lemmatization task for a given models
*OpenapiClient::TextTextLemmatizationApi* | [**get_versions_text_text_lemmatization_get**](docs/TextTextLemmatizationApi.md#get_versions_text_text_lemmatization_get) | **GET** /text/text/lemmatization/ | Get list of models available for lemmatization
*OpenapiClient::TextTextNamedEntityRecognitionApi* | [**apply_text_text_named_entity_recognition_post**](docs/TextTextNamedEntityRecognitionApi.md#apply_text_text_named_entity_recognition_post) | **POST** /text/text/named-entity-recognition/ | Apply model for the named-entity-recognition task for a given models
*OpenapiClient::TextTextNamedEntityRecognitionApi* | [**get_versions_text_text_named_entity_recognition_get**](docs/TextTextNamedEntityRecognitionApi.md#get_versions_text_text_named_entity_recognition_get) | **GET** /text/text/named-entity-recognition/ | Get list of models available for named-entity-recognition
*OpenapiClient::TextTextNextSentencePredictionApi* | [**apply_text_text_next_sentence_prediction_post**](docs/TextTextNextSentencePredictionApi.md#apply_text_text_next_sentence_prediction_post) | **POST** /text/text/next-sentence-prediction/ | Apply model for the next-sentence-prediction task for a given models
*OpenapiClient::TextTextNextSentencePredictionApi* | [**get_versions_text_text_next_sentence_prediction_get**](docs/TextTextNextSentencePredictionApi.md#get_versions_text_text_next_sentence_prediction_get) | **GET** /text/text/next-sentence-prediction/ | Get list of models available for next-sentence-prediction
*OpenapiClient::TextTextNextWordPredictionApi* | [**apply_text_text_next_word_prediction_post**](docs/TextTextNextWordPredictionApi.md#apply_text_text_next_word_prediction_post) | **POST** /text/text/next-word-prediction/ | Apply model for the next-word-prediction task for a given models
*OpenapiClient::TextTextNextWordPredictionApi* | [**get_versions_text_text_next_word_prediction_get**](docs/TextTextNextWordPredictionApi.md#get_versions_text_text_next_word_prediction_get) | **GET** /text/text/next-word-prediction/ | Get list of models available for next-word-prediction
*OpenapiClient::TextTextPluralApi* | [**apply_text_text_plural_post**](docs/TextTextPluralApi.md#apply_text_text_plural_post) | **POST** /text/text/plural/ | Apply model for the plural task for a given models
*OpenapiClient::TextTextPluralApi* | [**get_versions_text_text_plural_get**](docs/TextTextPluralApi.md#get_versions_text_text_plural_get) | **GET** /text/text/plural/ | Get list of models available for plural
*OpenapiClient::TextTextProgrammingLanguageGenerationApi* | [**apply_text_text_programming_language_generation_post**](docs/TextTextProgrammingLanguageGenerationApi.md#apply_text_text_programming_language_generation_post) | **POST** /text/text/programming-language-generation/ | Apply model for the programming-language-generation task for a given models
*OpenapiClient::TextTextProgrammingLanguageGenerationApi* | [**get_versions_text_text_programming_language_generation_get**](docs/TextTextProgrammingLanguageGenerationApi.md#get_versions_text_text_programming_language_generation_get) | **GET** /text/text/programming-language-generation/ | Get list of models available for programming-language-generation
*OpenapiClient::TextTextProgrammingLanguageIdentificationApi* | [**apply_text_text_programming_language_identification_post**](docs/TextTextProgrammingLanguageIdentificationApi.md#apply_text_text_programming_language_identification_post) | **POST** /text/text/programming-language-identification/ | Apply model for the programming-language-identification task for a given models
*OpenapiClient::TextTextProgrammingLanguageIdentificationApi* | [**get_versions_text_text_programming_language_identification_get**](docs/TextTextProgrammingLanguageIdentificationApi.md#get_versions_text_text_programming_language_identification_get) | **GET** /text/text/programming-language-identification/ | Get list of models available for programming-language-identification
*OpenapiClient::TextTextQuestionAnsweringApi* | [**apply_text_text_question_answering_post**](docs/TextTextQuestionAnsweringApi.md#apply_text_text_question_answering_post) | **POST** /text/text/question-answering/ | Apply model for the question-answering task for a given models
*OpenapiClient::TextTextQuestionAnsweringApi* | [**get_versions_text_text_question_answering_get**](docs/TextTextQuestionAnsweringApi.md#get_versions_text_text_question_answering_get) | **GET** /text/text/question-answering/ | Get list of models available for question-answering
*OpenapiClient::TextTextSentencePairModelingApi* | [**apply_text_text_sentence_pair_modeling_post**](docs/TextTextSentencePairModelingApi.md#apply_text_text_sentence_pair_modeling_post) | **POST** /text/text/sentence-pair-modeling/ | Apply model for the sentence-pair-modeling task for a given models
*OpenapiClient::TextTextSentencePairModelingApi* | [**get_versions_text_text_sentence_pair_modeling_get**](docs/TextTextSentencePairModelingApi.md#get_versions_text_text_sentence_pair_modeling_get) | **GET** /text/text/sentence-pair-modeling/ | Get list of models available for sentence-pair-modeling
*OpenapiClient::TextTextSentenceParaphraserApi* | [**apply_text_text_sentence_paraphraser_post**](docs/TextTextSentenceParaphraserApi.md#apply_text_text_sentence_paraphraser_post) | **POST** /text/text/sentence-paraphraser/ | Apply model for the sentence-paraphraser task for a given models
*OpenapiClient::TextTextSentenceParaphraserApi* | [**get_versions_text_text_sentence_paraphraser_get**](docs/TextTextSentenceParaphraserApi.md#get_versions_text_text_sentence_paraphraser_get) | **GET** /text/text/sentence-paraphraser/ | Get list of models available for sentence-paraphraser
*OpenapiClient::TextTextSentimentAnalysisApi* | [**apply_text_text_sentiment_analysis_post**](docs/TextTextSentimentAnalysisApi.md#apply_text_text_sentiment_analysis_post) | **POST** /text/text/sentiment-analysis/ | Apply model for the sentiment-analysis task for a given models
*OpenapiClient::TextTextSentimentAnalysisApi* | [**get_versions_text_text_sentiment_analysis_get**](docs/TextTextSentimentAnalysisApi.md#get_versions_text_text_sentiment_analysis_get) | **GET** /text/text/sentiment-analysis/ | Get list of models available for sentiment-analysis
*OpenapiClient::TextTextSimilarityApi* | [**apply_text_text_similarity_post**](docs/TextTextSimilarityApi.md#apply_text_text_similarity_post) | **POST** /text/text/similarity/ | Apply model for the similarity task for a given models
*OpenapiClient::TextTextSimilarityApi* | [**get_versions_text_text_similarity_get**](docs/TextTextSimilarityApi.md#get_versions_text_text_similarity_get) | **GET** /text/text/similarity/ | Get list of models available for similarity
*OpenapiClient::TextTextSummarizationApi* | [**apply_text_text_summarization_post**](docs/TextTextSummarizationApi.md#apply_text_text_summarization_post) | **POST** /text/text/summarization/ | Apply model for the summarization task for a given models
*OpenapiClient::TextTextSummarizationApi* | [**get_versions_text_text_summarization_get**](docs/TextTextSummarizationApi.md#get_versions_text_text_summarization_get) | **GET** /text/text/summarization/ | Get list of models available for summarization
*OpenapiClient::TextTextTranslationApi* | [**apply_text_text_translation_post**](docs/TextTextTranslationApi.md#apply_text_text_translation_post) | **POST** /text/text/translation/ | Apply model for the translation task for a given models
*OpenapiClient::TextTextTranslationApi* | [**get_versions_text_text_translation_get**](docs/TextTextTranslationApi.md#get_versions_text_text_translation_get) | **GET** /text/text/translation/ | Get list of models available for translation
*OpenapiClient::TextTextTransliterationApi* | [**apply_text_text_transliteration_post**](docs/TextTextTransliterationApi.md#apply_text_text_transliteration_post) | **POST** /text/text/transliteration/ | Apply model for the transliteration task for a given models
*OpenapiClient::TextTextTransliterationApi* | [**get_versions_text_text_transliteration_get**](docs/TextTextTransliterationApi.md#get_versions_text_text_transliteration_get) | **GET** /text/text/transliteration/ | Get list of models available for transliteration
*OpenapiClient::TextTextWordAlignmentApi* | [**apply_text_text_word_alignment_post**](docs/TextTextWordAlignmentApi.md#apply_text_text_word_alignment_post) | **POST** /text/text/word-alignment/ | Apply model for the word-alignment task for a given models
*OpenapiClient::TextTextWordAlignmentApi* | [**get_versions_text_text_word_alignment_get**](docs/TextTextWordAlignmentApi.md#get_versions_text_text_word_alignment_get) | **GET** /text/text/word-alignment/ | Get list of models available for word-alignment


## Documentation for Models

 - [OpenapiClient::BodyApplyImageImageBackgroundRemovalPost](docs/BodyApplyImageImageBackgroundRemovalPost.md)
 - [OpenapiClient::BodyApplyImageImageColorizationPost](docs/BodyApplyImageImageColorizationPost.md)
 - [OpenapiClient::BodyApplyImageImageFaceBluringPost](docs/BodyApplyImageImageFaceBluringPost.md)
 - [OpenapiClient::BodyApplyImageImageRestorationPost](docs/BodyApplyImageImageRestorationPost.md)
 - [OpenapiClient::BodyApplyImageImageSuperResolutionPost](docs/BodyApplyImageImageSuperResolutionPost.md)
 - [OpenapiClient::BodyApplyImageImageUncolorizationPost](docs/BodyApplyImageImageUncolorizationPost.md)
 - [OpenapiClient::HTTPValidationError](docs/HTTPValidationError.md)
 - [OpenapiClient::ValidationError](docs/ValidationError.md)


## Documentation for Authorization

 All endpoints do not require authorization.
