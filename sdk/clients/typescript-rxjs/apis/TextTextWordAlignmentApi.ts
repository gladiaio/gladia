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

import { Observable } from 'rxjs';
import { BaseAPI, RequiredError, HttpHeaders, HttpQuery, COLLECTION_FORMATS } from '../runtime';
import {
    HTTPValidationError,
} from '../models';

export interface ApplyTextTextWordAlignmentPostRequest {
    inputStringLanguage1?: string;
    inputStringLanguage2?: string;
    model?: ApplyTextTextWordAlignmentPostModelEnum;
}

/**
 * no description
 */
export class TextTextWordAlignmentApi extends BaseAPI {

    /**
     * Apply model for the word-alignment task for a given models
     */
    applyTextTextWordAlignmentPost(requestParameters: ApplyTextTextWordAlignmentPostRequest): Observable<object> {
        const queryParameters: HttpQuery = {};

        if (requestParameters.inputStringLanguage1 !== undefined && requestParameters.inputStringLanguage1 !== null) {
            queryParameters['input_string_language_1'] = requestParameters.inputStringLanguage1;
        }

        if (requestParameters.inputStringLanguage2 !== undefined && requestParameters.inputStringLanguage2 !== null) {
            queryParameters['input_string_language_2'] = requestParameters.inputStringLanguage2;
        }

        if (requestParameters.model !== undefined && requestParameters.model !== null) {
            queryParameters['model'] = requestParameters.model;
        }

        const headerParameters: HttpHeaders = {};

        return this.request<object>({
            path: `/text/text/word-alignment/`,
            method: 'POST',
            headers: headerParameters,
            query: queryParameters,
        });
    }

    /**
     * Get list of models available for word-alignment
     */
    getVersionsTextTextWordAlignmentGet(): Observable<object> {
        const queryParameters: HttpQuery = {};

        const headerParameters: HttpHeaders = {};

        return this.request<object>({
            path: `/text/text/word-alignment/`,
            method: 'GET',
            headers: headerParameters,
            query: queryParameters,
        });
    }

}

/**
    * @export
    * @enum {string}
    */
export enum ApplyTextTextWordAlignmentPostModelEnum {
    BertBaseMultilingualCased = 'bert-base-multilingual-cased'
}