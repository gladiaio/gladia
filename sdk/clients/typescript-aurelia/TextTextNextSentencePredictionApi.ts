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
 * applyTextTextNextSentencePredictionPost - parameters interface
 */
export interface IApplyTextTextNextSentencePredictionPostParams {
  sentence1?: string;
  sentence2?: string;
  model?: 'bert-base-uncased';
}

/**
 * getVersionsTextTextNextSentencePredictionGet - parameters interface
 */
export interface IGetVersionsTextTextNextSentencePredictionGetParams {
}

/**
 * TextTextNextSentencePredictionApi - API class
 */
@autoinject()
export class TextTextNextSentencePredictionApi extends Api {

  /**
   * Creates a new TextTextNextSentencePredictionApi class.
   *
   * @param httpClient The Aurelia HTTP client to be injected.
   * @param authStorage A storage for authentication data.
   */
  constructor(httpClient: HttpClient, authStorage: AuthStorage) {
    super(httpClient, authStorage);
  }

  /**
   * Apply model for the next-sentence-prediction task for a given models
   * @param params.sentence1 
   * @param params.sentence2 
   * @param params.model 
   */
  async applyTextTextNextSentencePredictionPost(params: IApplyTextTextNextSentencePredictionPostParams): Promise<object> {
    // Verify required parameters are set

    // Create URL to call
    const url = `${this.basePath}/text/text/next-sentence-prediction/`;

    const response = await this.httpClient.createRequest(url)
      // Set HTTP method
      .asPost()
      // Set query parameters
      .withParams({ 
        'sentence_1': params['sentence1'],
        'sentence_2': params['sentence2'],
        'model': params['model'],
      })

      // Send the request
      .send();

    if (response.statusCode < 200 || response.statusCode >= 300) {
      throw new Error(response.content);
    }

    // Extract the content
    return response.content;
  }

  /**
   * Get list of models available for next-sentence-prediction
   */
  async getVersionsTextTextNextSentencePredictionGet(): Promise<object> {
    // Verify required parameters are set

    // Create URL to call
    const url = `${this.basePath}/text/text/next-sentence-prediction/`;

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
