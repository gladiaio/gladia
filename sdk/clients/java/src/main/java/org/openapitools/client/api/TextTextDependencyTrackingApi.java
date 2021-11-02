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

public class TextTextDependencyTrackingApi {
    private ApiClient localVarApiClient;

    public TextTextDependencyTrackingApi() {
        this(Configuration.getDefaultApiClient());
    }

    public TextTextDependencyTrackingApi(ApiClient apiClient) {
        this.localVarApiClient = apiClient;
    }

    public ApiClient getApiClient() {
        return localVarApiClient;
    }

    public void setApiClient(ApiClient apiClient) {
        this.localVarApiClient = apiClient;
    }

    /**
     * Build call for applyTextTextDependencyTrackingPost
     * @param inputString  (optional, default to &quot;Text to analyzed&quot;)
     * @param model  (optional, default to &quot;LAL-Parser&quot;)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     */
    public okhttp3.Call applyTextTextDependencyTrackingPostCall(String inputString, String model, final ApiCallback _callback) throws ApiException {
        Object localVarPostBody = new Object();

        // create path and map variables
        String localVarPath = "/text/text/dependency-tracking/";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        if (inputString != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("input_string", inputString));
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
    private okhttp3.Call applyTextTextDependencyTrackingPostValidateBeforeCall(String inputString, String model, final ApiCallback _callback) throws ApiException {
        

        okhttp3.Call localVarCall = applyTextTextDependencyTrackingPostCall(inputString, model, _callback);
        return localVarCall;

    }

    /**
     * Apply model for the dependency-tracking task for a given models
     * 
     * @param inputString  (optional, default to &quot;Text to analyzed&quot;)
     * @param model  (optional, default to &quot;LAL-Parser&quot;)
     * @return Object
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     */
    public Object applyTextTextDependencyTrackingPost(String inputString, String model) throws ApiException {
        ApiResponse<Object> localVarResp = applyTextTextDependencyTrackingPostWithHttpInfo(inputString, model);
        return localVarResp.getData();
    }

    /**
     * Apply model for the dependency-tracking task for a given models
     * 
     * @param inputString  (optional, default to &quot;Text to analyzed&quot;)
     * @param model  (optional, default to &quot;LAL-Parser&quot;)
     * @return ApiResponse&lt;Object&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     */
    public ApiResponse<Object> applyTextTextDependencyTrackingPostWithHttpInfo(String inputString, String model) throws ApiException {
        okhttp3.Call localVarCall = applyTextTextDependencyTrackingPostValidateBeforeCall(inputString, model, null);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Apply model for the dependency-tracking task for a given models (asynchronously)
     * 
     * @param inputString  (optional, default to &quot;Text to analyzed&quot;)
     * @param model  (optional, default to &quot;LAL-Parser&quot;)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     */
    public okhttp3.Call applyTextTextDependencyTrackingPostAsync(String inputString, String model, final ApiCallback<Object> _callback) throws ApiException {

        okhttp3.Call localVarCall = applyTextTextDependencyTrackingPostValidateBeforeCall(inputString, model, _callback);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getVersionsTextTextDependencyTrackingGet
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     */
    public okhttp3.Call getVersionsTextTextDependencyTrackingGetCall(final ApiCallback _callback) throws ApiException {
        Object localVarPostBody = new Object();

        // create path and map variables
        String localVarPath = "/text/text/dependency-tracking/";

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
    private okhttp3.Call getVersionsTextTextDependencyTrackingGetValidateBeforeCall(final ApiCallback _callback) throws ApiException {
        

        okhttp3.Call localVarCall = getVersionsTextTextDependencyTrackingGetCall(_callback);
        return localVarCall;

    }

    /**
     * Get list of models available for dependency-tracking
     * 
     * @return Object
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     */
    public Object getVersionsTextTextDependencyTrackingGet() throws ApiException {
        ApiResponse<Object> localVarResp = getVersionsTextTextDependencyTrackingGetWithHttpInfo();
        return localVarResp.getData();
    }

    /**
     * Get list of models available for dependency-tracking
     * 
     * @return ApiResponse&lt;Object&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     */
    public ApiResponse<Object> getVersionsTextTextDependencyTrackingGetWithHttpInfo() throws ApiException {
        okhttp3.Call localVarCall = getVersionsTextTextDependencyTrackingGetValidateBeforeCall(null);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Get list of models available for dependency-tracking (asynchronously)
     * 
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     */
    public okhttp3.Call getVersionsTextTextDependencyTrackingGetAsync(final ApiCallback<Object> _callback) throws ApiException {

        okhttp3.Call localVarCall = getVersionsTextTextDependencyTrackingGetValidateBeforeCall(_callback);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
}