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

export interface ApplyTextTextNamedEntityRecognitionPostRequest {
    text?: string;
    model?: ApplyTextTextNamedEntityRecognitionPostModelEnum;
}

/**
 * no description
 */
export class TextTextNamedEntityRecognitionApi extends runtime.BaseAPI {

    /**
     * Apply model for the named-entity-recognition task for a given models
     */
    async applyTextTextNamedEntityRecognitionPostRaw(requestParameters: ApplyTextTextNamedEntityRecognitionPostRequest): Promise<runtime.ApiResponse<object>> {
        const queryParameters: runtime.HTTPQuery = {};

        if (requestParameters.text !== undefined) {
            queryParameters['text'] = requestParameters.text;
        }

        if (requestParameters.model !== undefined) {
            queryParameters['model'] = requestParameters.model;
        }

        const headerParameters: runtime.HTTPHeaders = {};

        const response = await this.request({
            path: `/text/text/named-entity-recognition/`,
            method: 'POST',
            headers: headerParameters,
            query: queryParameters,
        });

        return new runtime.TextApiResponse(response);
    }

    /**
     * Apply model for the named-entity-recognition task for a given models
     */
    async applyTextTextNamedEntityRecognitionPost(requestParameters: ApplyTextTextNamedEntityRecognitionPostRequest): Promise<object> {
        const response = await this.applyTextTextNamedEntityRecognitionPostRaw(requestParameters);
        return await response.value();
    }

    /**
     * Get list of models available for named-entity-recognition
     */
    async getVersionsTextTextNamedEntityRecognitionGetRaw(): Promise<runtime.ApiResponse<object>> {
        const queryParameters: runtime.HTTPQuery = {};

        const headerParameters: runtime.HTTPHeaders = {};

        const response = await this.request({
            path: `/text/text/named-entity-recognition/`,
            method: 'GET',
            headers: headerParameters,
            query: queryParameters,
        });

        return new runtime.TextApiResponse(response);
    }

    /**
     * Get list of models available for named-entity-recognition
     */
    async getVersionsTextTextNamedEntityRecognitionGet(): Promise<object> {
        const response = await this.getVersionsTextTextNamedEntityRecognitionGetRaw();
        return await response.value();
    }

}

/**
    * @export
    * @enum {string}
    */
export enum ApplyTextTextNamedEntityRecognitionPostModelEnum {
    DbmdzBertLargeCasedFinetunedConll03English = 'dbmdz-bert-large-cased-finetuned-conll03-english'
}