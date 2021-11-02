-module(openapi_text_text_sentence_paraphraser_api).

-export([apply_text_text_sentence_paraphraser_post/1, apply_text_text_sentence_paraphraser_post/2,
         get_versions_text_text_sentence_paraphraser_get/1, get_versions_text_text_sentence_paraphraser_get/2]).

-define(BASE_URL, "").

%% @doc Apply model for the sentence-paraphraser task for a given models
%% 
-spec apply_text_text_sentence_paraphraser_post(ctx:ctx()) -> {ok, maps:map(), openapi_utils:response_info()} | {ok, hackney:client_ref()} | {error, term(), openapi_utils:response_info()}.
apply_text_text_sentence_paraphraser_post(Ctx) ->
    apply_text_text_sentence_paraphraser_post(Ctx, #{}).

-spec apply_text_text_sentence_paraphraser_post(ctx:ctx(), maps:map()) -> {ok, maps:map(), openapi_utils:response_info()} | {ok, hackney:client_ref()} | {error, term(), openapi_utils:response_info()}.
apply_text_text_sentence_paraphraser_post(Ctx, Optional) ->
    _OptionalParams = maps:get(params, Optional, #{}),
    Cfg = maps:get(cfg, Optional, application:get_env(kuberl, config, #{})),

    Method = post,
    Path = ["/text/text/sentence-paraphraser/"],
    QS = lists:flatten([])++openapi_utils:optional_params(['context', 'model'], _OptionalParams),
    Headers = [],
    Body1 = [],
    ContentTypeHeader = openapi_utils:select_header_content_type([]),
    Opts = maps:get(hackney_opts, Optional, []),

    openapi_utils:request(Ctx, Method, [?BASE_URL, Path], QS, ContentTypeHeader++Headers, Body1, Opts, Cfg).

%% @doc Get list of models available for sentence-paraphraser
%% 
-spec get_versions_text_text_sentence_paraphraser_get(ctx:ctx()) -> {ok, maps:map(), openapi_utils:response_info()} | {ok, hackney:client_ref()} | {error, term(), openapi_utils:response_info()}.
get_versions_text_text_sentence_paraphraser_get(Ctx) ->
    get_versions_text_text_sentence_paraphraser_get(Ctx, #{}).

-spec get_versions_text_text_sentence_paraphraser_get(ctx:ctx(), maps:map()) -> {ok, maps:map(), openapi_utils:response_info()} | {ok, hackney:client_ref()} | {error, term(), openapi_utils:response_info()}.
get_versions_text_text_sentence_paraphraser_get(Ctx, Optional) ->
    _OptionalParams = maps:get(params, Optional, #{}),
    Cfg = maps:get(cfg, Optional, application:get_env(kuberl, config, #{})),

    Method = get,
    Path = ["/text/text/sentence-paraphraser/"],
    QS = [],
    Headers = [],
    Body1 = [],
    ContentTypeHeader = openapi_utils:select_header_content_type([]),
    Opts = maps:get(hackney_opts, Optional, []),

    openapi_utils:request(Ctx, Method, [?BASE_URL, Path], QS, ContentTypeHeader++Headers, Body1, Opts, Cfg).

