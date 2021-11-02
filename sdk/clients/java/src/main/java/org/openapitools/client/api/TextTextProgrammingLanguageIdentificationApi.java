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

public class TextTextProgrammingLanguageIdentificationApi {
    private ApiClient localVarApiClient;

    public TextTextProgrammingLanguageIdentificationApi() {
        this(Configuration.getDefaultApiClient());
    }

    public TextTextProgrammingLanguageIdentificationApi(ApiClient apiClient) {
        this.localVarApiClient = apiClient;
    }

    public ApiClient getApiClient() {
        return localVarApiClient;
    }

    public void setApiClient(ApiClient apiClient) {
        this.localVarApiClient = apiClient;
    }

    /**
     * Build call for applyTextTextProgrammingLanguageIdentificationPost
     * @param text  (optional, default to &quot;def is_palendrome(s):&quot;)
     * @param model  (optional, default to &quot;aliostad&quot;)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     */
    public okhttp3.Call applyTextTextProgrammingLanguageIdentificationPostCall(String text, String model, final ApiCallback _callback) throws ApiException {
        Object localVarPostBody = new Object();

        // create path and map variables
        String localVarPath = "/text/text/programming-language-identification/";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        if (text != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("text", text));
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
    private okhttp3.Call applyTextTextProgrammingLanguageIdentificationPostValidateBeforeCall(String text, String model, final ApiCallback _callback) throws ApiException {
        

        okhttp3.Call localVarCall = applyTextTextProgrammingLanguageIdentificationPostCall(text, model, _callback);
        return localVarCall;

    }

    /**
     * Apply model for the programming-language-identification task for a given models
     * 
     * @param text  (optional, default to &quot;def is_palendrome(s):&quot;)
     * @param model  (optional, default to &quot;aliostad&quot;)
     * @return Object
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     */
    public Object applyTextTextProgrammingLanguageIdentificationPost(String text, String model) throws ApiException {
        ApiResponse<Object> localVarResp = applyTextTextProgrammingLanguageIdentificationPostWithHttpInfo(text, model);
        return localVarResp.getData();
    }

    /**
     * Apply model for the programming-language-identification task for a given models
     * 
     * @param text  (optional, default to &quot;def is_palendrome(s):&quot;)
     * @param model  (optional, default to &quot;aliostad&quot;)
     * @return ApiResponse&lt;Object&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     */
    public ApiResponse<Object> applyTextTextProgrammingLanguageIdentificationPostWithHttpInfo(String text, String model) throws ApiException {
        okhttp3.Call localVarCall = applyTextTextProgrammingLanguageIdentificationPostValidateBeforeCall(text, model, null);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Apply model for the programming-language-identification task for a given models (asynchronously)
     * 
     * @param text  (optional, default to &quot;def is_palendrome(s):&quot;)
     * @param model  (optional, default to &quot;aliostad&quot;)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     */
    public okhttp3.Call applyTextTextProgrammingLanguageIdentificationPostAsync(String text, String model, final ApiCallback<Object> _callback) throws ApiException {

        okhttp3.Call localVarCall = applyTextTextProgrammingLanguageIdentificationPostValidateBeforeCall(text, model, _callback);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getVersionsTextTextProgrammingLanguageIdentificationGet
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     */
    public okhttp3.Call getVersionsTextTextProgrammingLanguageIdentificationGetCall(final ApiCallback _callback) throws ApiException {
        Object localVarPostBody = new Object();

        // create path and map variables
        String localVarPath = "/text/text/programming-language-identification/";

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
    private okhttp3.Call getVersionsTextTextProgrammingLanguageIdentificationGetValidateBeforeCall(final ApiCallback _callback) throws ApiException {
        

        okhttp3.Call localVarCall = getVersionsTextTextProgrammingLanguageIdentificationGetCall(_callback);
        return localVarCall;

    }

    /**
     * Get list of models available for programming-language-identification
     * 
     * @return Object
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     */
    public Object getVersionsTextTextProgrammingLanguageIdentificationGet() throws ApiException {
        ApiResponse<Object> localVarResp = getVersionsTextTextProgrammingLanguageIdentificationGetWithHttpInfo();
        return localVarResp.getData();
    }

    /**
     * Get list of models available for programming-language-identification
     * 
     * @return ApiResponse&lt;Object&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     */
    public ApiResponse<Object> getVersionsTextTextProgrammingLanguageIdentificationGetWithHttpInfo() throws ApiException {
        okhttp3.Call localVarCall = getVersionsTextTextProgrammingLanguageIdentificationGetValidateBeforeCall(null);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Get list of models available for programming-language-identification (asynchronously)
     * 
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     */
    public okhttp3.Call getVersionsTextTextProgrammingLanguageIdentificationGetAsync(final ApiCallback<Object> _callback) throws ApiException {

        okhttp3.Call localVarCall = getVersionsTextTextProgrammingLanguageIdentificationGetValidateBeforeCall(_callback);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
}