package org.openapitools.client.api {

import org.openapitools.common.ApiInvoker;
import org.openapitools.exception.ApiErrorCodes;
import org.openapitools.exception.ApiError;
import org.openapitools.common.ApiUserCredentials;
import org.openapitools.event.Response;
import org.openapitools.common.OpenApi;
import org.openapitools.client.model.HTTPValidationError;
import org.openapitools.client.model.Object;

import mx.rpc.AsyncToken;
import mx.utils.UIDUtil;
import flash.utils.Dictionary;
import flash.events.EventDispatcher;

public class TextTextAutocorrectApi extends OpenApi {
    /**
    * Constructor for the TextTextAutocorrectApi api client
    * @param apiCredentials Wrapper object for tokens and hostName required towards authentication
    * @param eventDispatcher Optional event dispatcher that when provided is used by the SDK to dispatch any Response
    */
    public function TextTextAutocorrectApi(apiCredentials: ApiUserCredentials, eventDispatcher: EventDispatcher = null) {
        super(apiCredentials, eventDispatcher);
    }

        public static const event_apply_text_text_autocorrect_post: String = "apply_text_text_autocorrect_post";
        public static const event_get_versions_text_text_autocorrect_get: String = "get_versions_text_text_autocorrect_get";


    /*
     * Returns Object 
     */
    public function apply_text_text_autocorrect_post (sentence: String, model: String): String {
        // create path and map variables
        var path: String = "/text/text/autocorrect/".replace(/{format}/g,"xml");

        // query params
        var queryParams: Dictionary = new Dictionary();
        var headerParams: Dictionary = new Dictionary();

        // verify required params are set
        if(        // verify required params are set
        if() {
            throw new ApiError(400, "missing required params");
        }
) {
            throw new ApiError(400, "missing required params");
        }

        if("null" != String(sentence))
            queryParams["sentence"] = toPathValue(sentence);
if("null" != String(model))
            queryParams["model"] = toPathValue(model);

        
        var token:AsyncToken = getApiInvoker().invokeAPI(path, "POST", queryParams, null, headerParams);

        var requestId: String = getUniqueId();

        token.requestId = requestId;
        token.completionEventType = "apply_text_text_autocorrect_post";

        token.returnType = Object;
        return requestId;

    }

    /*
     * Returns Object 
     */
    public function get_versions_text_text_autocorrect_get (): String {
        // create path and map variables
        var path: String = "/text/text/autocorrect/".replace(/{format}/g,"xml");

        // query params
        var queryParams: Dictionary = new Dictionary();
        var headerParams: Dictionary = new Dictionary();


        
        
        var token:AsyncToken = getApiInvoker().invokeAPI(path, "GET", queryParams, null, headerParams);

        var requestId: String = getUniqueId();

        token.requestId = requestId;
        token.completionEventType = "get_versions_text_text_autocorrect_get";

        token.returnType = Object;
        return requestId;

    }
}
}