// tslint:disable
/**
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


import * as runtime from '../runtime';
import {
    HTTPValidationError,
    HTTPValidationErrorFromJSON,
    HTTPValidationErrorToJSON,
} from '../models';

export interface ApplyTextTextEmotionRecognitionPostRequest {
    text?: string;
    model?: string;
}

/**
 * no description
 */
export class TextTextEmotionRecognitionApi extends runtime.BaseAPI {

    /**
     * Apply model for the emotion-recognition task for a given models
     */
    async applyTextTextEmotionRecognitionPostRaw(requestParameters: ApplyTextTextEmotionRecognitionPostRequest): Promise<runtime.ApiResponse<object>> {
        const queryParameters: runtime.HTTPQuery = {};

        if (requestParameters.text !== undefined) {
            queryParameters['text'] = requestParameters.text;
        }

        if (requestParameters.model !== undefined) {
            queryParameters['model'] = requestParameters.model;
        }

        const headerParameters: runtime.HTTPHeaders = {};

        const response = await this.request({
            path: `/text/text/emotion-recognition/`,
            method: 'POST',
            headers: headerParameters,
            query: queryParameters,
        });

        return new runtime.TextApiResponse(response);
    }

    /**
     * Apply model for the emotion-recognition task for a given models
     */
    async applyTextTextEmotionRecognitionPost(requestParameters: ApplyTextTextEmotionRecognitionPostRequest): Promise<object> {
        const response = await this.applyTextTextEmotionRecognitionPostRaw(requestParameters);
        return await response.value();
    }

    /**
     * Get list of models available for emotion-recognition
     */
    async getVersionsTextTextEmotionRecognitionGetRaw(): Promise<runtime.ApiResponse<object>> {
        const queryParameters: runtime.HTTPQuery = {};

        const headerParameters: runtime.HTTPHeaders = {};

        const response = await this.request({
            path: `/text/text/emotion-recognition/`,
            method: 'GET',
            headers: headerParameters,
            query: queryParameters,
        });

        return new runtime.TextApiResponse(response);
    }

    /**
     * Get list of models available for emotion-recognition
     */
    async getVersionsTextTextEmotionRecognitionGet(): Promise<object> {
        const response = await this.getVersionsTextTextEmotionRecognitionGetRaw();
        return await response.value();
    }

}