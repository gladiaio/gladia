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

import { autoinject } from 'aurelia-framework';
import { HttpClient } from 'aurelia-http-client';
import { Api } from './Api';
import { AuthStorage } from './AuthStorage';
import {
} from './models';

/**
 * applyImageImageSuperResolutionPost - parameters interface
 */
export interface IApplyImageImageSuperResolutionPostParams {
  image: any;
  model?: string;
}

/**
 * getVersionsImageImageSuperResolutionGet - parameters interface
 */
export interface IGetVersionsImageImageSuperResolutionGetParams {
}

/**
 * ImageImageSuperResolutionApi - API class
 */
@autoinject()
export class ImageImageSuperResolutionApi extends Api {

  /**
   * Creates a new ImageImageSuperResolutionApi class.
   *
   * @param httpClient The Aurelia HTTP client to be injected.
   * @param authStorage A storage for authentication data.
   */
  constructor(httpClient: HttpClient, authStorage: AuthStorage) {
    super(httpClient, authStorage);
  }

  /**
   * Apply model for the super-resolution task for a given models
   * @param params.image 
   * @param params.model 
   */
  async applyImageImageSuperResolutionPost(params: IApplyImageImageSuperResolutionPostParams): Promise<object> {
    // Verify required parameters are set
    this.ensureParamIsSet('applyImageImageSuperResolutionPost', params, 'image');

    // Create URL to call
    const url = `${this.basePath}/image/image/super-resolution/`;

    const response = await this.httpClient.createRequest(url)
      // Set HTTP method
      .asPost()
      // Set query parameters
      .withParams({ 
        'model': params['model'],
      })
      // Encode form parameters
      .withHeader('content-type', 'application/x-www-form-urlencoded')
      .withContent(this.queryString({ 
        'image': params['image'],
      }))

      // Send the request
      .send();

    if (response.statusCode < 200 || response.statusCode >= 300) {
      throw new Error(response.content);
    }

    // Extract the content
    return response.content;
  }

  /**
   * Get list of models available for super-resolution
   */
  async getVersionsImageImageSuperResolutionGet(): Promise<object> {
    // Verify required parameters are set

    // Create URL to call
    const url = `${this.basePath}/image/image/super-resolution/`;

    const response = await this.httpClient.createRequest(url)
      // Set HTTP method
      .asGet()

      // Send the request
      .send();

    if (response.statusCode < 200 || response.statusCode >= 300) {
      throw new Error(response.content);
    }

    // Extract the content
    return response.content;
  }

}
