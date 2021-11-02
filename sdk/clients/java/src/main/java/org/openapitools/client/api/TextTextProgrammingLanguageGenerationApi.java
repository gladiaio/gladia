/*
 * FastAPI
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 0.1.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.openapitools.client.api;

import org.openapitools.client.ApiCallback;
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.ApiResponse;
import org.openapitools.client.Configuration;
import org.openapitools.client.Pair;
import org.openapitools.client.ProgressRequestBody;
import org.openapitools.client.ProgressResponseBody;

import com.google.gson.reflect.TypeToken;

import java.io.IOException;


import org.openapitools.client.model.HTTPValidationError;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class TextTextProgrammingLanguageGenerationApi {
    private ApiClient localVarApiClient;

    public TextTextProgrammingLanguageGenerationApi() {
        this(Configuration.getDefaultApiClient());
    }

    public TextTextProgrammingLanguageGenerationApi(ApiClient apiClient) {
        this.localVarApiClient = apiClient;
    }

    public ApiClient getApiClient() {
        return localVarApiClient;
    }

    public void setApiClient(ApiClient apiClient) {
        this.localVarApiClient = apiClient;
    }

    /**
     * Build call for applyTextTextProgrammingLanguageGenerationPost
     * @param codeSnippet  (optional, default to &quot;def is_palendrome(s):&quot;)
     * @param model  (optional, default to sentdex-GPyT)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     */
    public okhttp3.Call applyTextTextProgrammingLanguageGenerationPostCall(String codeSnippet, String model, final ApiCallback _callback) throws ApiException {
        Object localVarPostBody = new Object();

        // create path and map variables
        String localVarPath = "/text/text/programming-language-generation/";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        if (codeSnippet != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("code_snippet", codeSnippet));
        }

        if (model != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("model", model));
        }

        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();
        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
            
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        localVarHeaderParams.put("Content-Type", localVarContentType);

        String[] localVarAuthNames = new String[] {  };
        return localVarApiClient.buildCall(localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call applyTextTextProgrammingLanguageGenerationPostValidateBeforeCall(String codeSnippet, String model, final ApiCallback _callback) throws ApiException {
        

        okhttp3.Call localVarCall = applyTextTextProgrammingLanguageGenerationPostCall(codeSnippet, model, _callback);
        return localVarCall;

    }

    /**
     * Apply model for the programming-language-generation task for a given models
     * 
     * @param codeSnippet  (optional, default to &quot;def is_palendrome(s):&quot;)
     * @param model  (optional, default to sentdex-GPyT)
     * @return Object
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     */
    public Object applyTextTextProgrammingLanguageGenerationPost(String codeSnippet, String model) throws ApiException {
        ApiResponse<Object> localVarResp = applyTextTextProgrammingLanguageGenerationPostWithHttpInfo(codeSnippet, model);
        return localVarResp.getData();
    }

    /**
     * Apply model for the programming-language-generation task for a given models
     * 
     * @param codeSnippet  (optional, default to &quot;def is_palendrome(s):&quot;)
     * @param model  (optional, default to sentdex-GPyT)
     * @return ApiResponse&lt;Object&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     */
    public ApiResponse<Object> applyTextTextProgrammingLanguageGenerationPostWithHttpInfo(String codeSnippet, String model) throws ApiException {
        okhttp3.Call localVarCall = applyTextTextProgrammingLanguageGenerationPostValidateBeforeCall(codeSnippet, model, null);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Apply model for the programming-language-generation task for a given models (asynchronously)
     * 
     * @param codeSnippet  (optional, default to &quot;def is_palendrome(s):&quot;)
     * @param model  (optional, default to sentdex-GPyT)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     */
    public okhttp3.Call applyTextTextProgrammingLanguageGenerationPostAsync(String codeSnippet, String model, final ApiCallback<Object> _callback) throws ApiException {

        okhttp3.Call localVarCall = applyTextTextProgrammingLanguageGenerationPostValidateBeforeCall(codeSnippet, model, _callback);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getVersionsTextTextProgrammingLanguageGenerationGet
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     */
    public okhttp3.Call getVersionsTextTextProgrammingLanguageGenerationGetCall(final ApiCallback _callback) throws ApiException {
        Object localVarPostBody = new Object();

        // create path and map variables
        String localVarPath = "/text/text/programming-language-generation/";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();
        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
            
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        localVarHeaderParams.put("Content-Type", localVarContentType);

        String[] localVarAuthNames = new String[] {  };
        return localVarApiClient.buildCall(localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call getVersionsTextTextProgrammingLanguageGenerationGetValidateBeforeCall(final ApiCallback _callback) throws ApiException {
        

        okhttp3.Call localVarCall = getVersionsTextTextProgrammingLanguageGenerationGetCall(_callback);
        return localVarCall;

    }

    /**
     * Get list of models available for programming-language-generation
     * 
     * @return Object
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     */
    public Object getVersionsTextTextProgrammingLanguageGenerationGet() throws ApiException {
        ApiResponse<Object> localVarResp = getVersionsTextTextProgrammingLanguageGenerationGetWithHttpInfo();
        return localVarResp.getData();
    }

    /**
     * Get list of models available for programming-language-generation
     * 
     * @return ApiResponse&lt;Object&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     */
    public ApiResponse<Object> getVersionsTextTextProgrammingLanguageGenerationGetWithHttpInfo() throws ApiException {
        okhttp3.Call localVarCall = getVersionsTextTextProgrammingLanguageGenerationGetValidateBeforeCall(null);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Get list of models available for programming-language-generation (asynchronously)
     * 
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     */
    public okhttp3.Call getVersionsTextTextProgrammingLanguageGenerationGetAsync(final ApiCallback<Object> _callback) throws ApiException {

        okhttp3.Call localVarCall = getVersionsTextTextProgrammingLanguageGenerationGetValidateBeforeCall(_callback);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
}