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
/* tslint:disable:no-unused-variable member-ordering */

import { Observable } from "rxjs/Observable";
import 'rxjs/add/operator/map';
import 'rxjs/add/operator/toPromise';
import IHttpClient from "../IHttpClient";
import { inject, injectable } from "inversify";
import { IAPIConfiguration } from "../IAPIConfiguration";
import { Headers } from "../Headers";
import HttpResponse from "../HttpResponse";

import { HTTPValidationError } from '../model/hTTPValidationError';

import { COLLECTION_FORMATS }  from '../variables';



@injectable()
export class TextTextSummarizationService {
    private basePath: string = 'http://localhost';

    constructor(@inject("IApiHttpClient") private httpClient: IHttpClient,
        @inject("IAPIConfiguration") private APIConfiguration: IAPIConfiguration ) {
        if(this.APIConfiguration.basePath)
            this.basePath = this.APIConfiguration.basePath;
    }

    /**
     * Apply model for the summarization task for a given models
     * 
     * @param text 
     * @param sourceLanguage 
     * @param maxLength 
     * @param minLength 
     * @param model 
     
     */
    public applyTextTextSummarizationPost(text?: string, sourceLanguage?: string, maxLength?: number, minLength?: number, model?: 'distilbart-cnn-12-6', observe?: 'body', headers?: Headers): Observable<object>;
    public applyTextTextSummarizationPost(text?: string, sourceLanguage?: string, maxLength?: number, minLength?: number, model?: 'distilbart-cnn-12-6', observe?: 'response', headers?: Headers): Observable<HttpResponse<object>>;
    public applyTextTextSummarizationPost(text?: string, sourceLanguage?: string, maxLength?: number, minLength?: number, model?: 'distilbart-cnn-12-6', observe: any = 'body', headers: Headers = {}): Observable<any> {
        let queryParameters: string[] = [];
        if (text !== undefined) {
            queryParameters.push("text="+encodeURIComponent(String(text)));
        }
        if (sourceLanguage !== undefined) {
            queryParameters.push("sourceLanguage="+encodeURIComponent(String(sourceLanguage)));
        }
        if (maxLength !== undefined) {
            queryParameters.push("maxLength="+encodeURIComponent(String(maxLength)));
        }
        if (minLength !== undefined) {
            queryParameters.push("minLength="+encodeURIComponent(String(minLength)));
        }
        if (model !== undefined) {
            queryParameters.push("model="+encodeURIComponent(String(model)));
        }

        headers['Accept'] = 'application/json';

        const response: Observable<HttpResponse<object>> = this.httpClient.post(`${this.basePath}/text/text/summarization/?${queryParameters.join('&')}`, headers);
        if (observe == 'body') {
               return response.map(httpResponse => <object>(httpResponse.response));
        }
        return response;
    }


    /**
     * Get list of models available for summarization
     * 
     
     */
    public getVersionsTextTextSummarizationGet(observe?: 'body', headers?: Headers): Observable<object>;
    public getVersionsTextTextSummarizationGet(observe?: 'response', headers?: Headers): Observable<HttpResponse<object>>;
    public getVersionsTextTextSummarizationGet(observe: any = 'body', headers: Headers = {}): Observable<any> {
        headers['Accept'] = 'application/json';

        const response: Observable<HttpResponse<object>> = this.httpClient.get(`${this.basePath}/text/text/summarization/`, headers);
        if (observe == 'body') {
               return response.map(httpResponse => <object>(httpResponse.response));
        }
        return response;
    }

}