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

export interface ApplyTextTextEntityExtractionPostRequest {
    inputString?: string;
    model?: string;
}

/**
 * no description
 */
export class TextTextEntityExtractionApi extends runtime.BaseAPI {

    /**
     * Apply model for the entity-extraction task for a given models
     */
    async applyTextTextEntityExtractionPostRaw(requestParameters: ApplyTextTextEntityExtractionPostRequest): Promise<runtime.ApiResponse<object>> {
        const queryParameters: runtime.HTTPQuery = {};

        if (requestParameters.inputString !== undefined) {
            queryParameters['input_string'] = requestParameters.inputString;
        }

        if (requestParameters.model !== undefined) {
            queryParameters['model'] = requestParameters.model;
        }

        const headerParameters: runtime.HTTPHeaders = {};

        const response = await this.request({
            path: `/text/text/entity-extraction/`,
            method: 'POST',
            headers: headerParameters,
            query: queryParameters,
        });

        return new runtime.TextApiResponse(response);
    }

    /**
     * Apply model for the entity-extraction task for a given models
     */
    async applyTextTextEntityExtractionPost(requestParameters: ApplyTextTextEntityExtractionPostRequest): Promise<object> {
        const response = await this.applyTextTextEntityExtractionPostRaw(requestParameters);
        return await response.value();
    }

    /**
     * Get list of models available for entity-extraction
     */
    async getVersionsTextTextEntityExtractionGetRaw(): Promise<runtime.ApiResponse<object>> {
        const queryParameters: runtime.HTTPQuery = {};

        const headerParameters: runtime.HTTPHeaders = {};

        const response = await this.request({
            path: `/text/text/entity-extraction/`,
            method: 'GET',
            headers: headerParameters,
            query: queryParameters,
        });

        return new runtime.TextApiResponse(response);
    }

    /**
     * Get list of models available for entity-extraction
     */
    async getVersionsTextTextEntityExtractionGet(): Promise<object> {
        const response = await this.getVersionsTextTextEntityExtractionGetRaw();
        return await response.value();
    }

}