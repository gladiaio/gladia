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

export interface ApplyImageImageColorizationPostRequest {
    image: Blob;
    model?: ApplyImageImageColorizationPostModelEnum;
}

/**
 * no description
 */
export class ImageImageColorizationApi extends runtime.BaseAPI {

    /**
     * Apply model for the colorization task for a given models
     */
    async applyImageImageColorizationPostRaw(requestParameters: ApplyImageImageColorizationPostRequest): Promise<runtime.ApiResponse<object>> {
        if (requestParameters.image === null || requestParameters.image === undefined) {
            throw new runtime.RequiredError('image','Required parameter requestParameters.image was null or undefined when calling applyImageImageColorizationPost.');
        }

        const queryParameters: runtime.HTTPQuery = {};

        if (requestParameters.model !== undefined) {
            queryParameters['model'] = requestParameters.model;
        }

        const headerParameters: runtime.HTTPHeaders = {};

        const formData = new FormData();
        if (requestParameters.image !== undefined) {
            formData.append('image', requestParameters.image as any);
        }

        const response = await this.request({
            path: `/image/image/colorization/`,
            method: 'POST',
            headers: headerParameters,
            query: queryParameters,
            body: formData,
        });

        return new runtime.TextApiResponse(response);
    }

    /**
     * Apply model for the colorization task for a given models
     */
    async applyImageImageColorizationPost(requestParameters: ApplyImageImageColorizationPostRequest): Promise<object> {
        const response = await this.applyImageImageColorizationPostRaw(requestParameters);
        return await response.value();
    }

    /**
     * Get list of models available for colorization
     */
    async getVersionsImageImageColorizationGetRaw(): Promise<runtime.ApiResponse<object>> {
        const queryParameters: runtime.HTTPQuery = {};

        const headerParameters: runtime.HTTPHeaders = {};

        const response = await this.request({
            path: `/image/image/colorization/`,
            method: 'GET',
            headers: headerParameters,
            query: queryParameters,
        });

        return new runtime.TextApiResponse(response);
    }

    /**
     * Get list of models available for colorization
     */
    async getVersionsImageImageColorizationGet(): Promise<object> {
        const response = await this.getVersionsImageImageColorizationGetRaw();
        return await response.value();
    }

}

/**
    * @export
    * @enum {string}
    */
export enum ApplyImageImageColorizationPostModelEnum {
    Artistic = 'deoldify-artistic',
    Stable = 'deoldify-stable'
}