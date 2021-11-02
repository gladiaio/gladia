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
export class TextTextWordAlignmentService {
    private basePath: string = 'http://localhost';

    constructor(@inject("IApiHttpClient") private httpClient: IHttpClient,
        @inject("IAPIConfiguration") private APIConfiguration: IAPIConfiguration ) {
        if(this.APIConfiguration.basePath)
            this.basePath = this.APIConfiguration.basePath;
    }

    /**
     * Apply model for the word-alignment task for a given models
     * 
     * @param inputStringLanguage1 
     * @param inputStringLanguage2 
     * @param model 
     
     */
    public applyTextTextWordAlignmentPost(inputStringLanguage1?: string, inputStringLanguage2?: string, model?: 'bert-base-multilingual-cased', observe?: 'body', headers?: Headers): Observable<object>;
    public applyTextTextWordAlignmentPost(inputStringLanguage1?: string, inputStringLanguage2?: string, model?: 'bert-base-multilingual-cased', observe?: 'response', headers?: Headers): Observable<HttpResponse<object>>;
    public applyTextTextWordAlignmentPost(inputStringLanguage1?: string, inputStringLanguage2?: string, model?: 'bert-base-multilingual-cased', observe: any = 'body', headers: Headers = {}): Observable<any> {
        let queryParameters: string[] = [];
        if (inputStringLanguage1 !== undefined) {
            queryParameters.push("inputStringLanguage1="+encodeURIComponent(String(inputStringLanguage1)));
        }
        if (inputStringLanguage2 !== undefined) {
            queryParameters.push("inputStringLanguage2="+encodeURIComponent(String(inputStringLanguage2)));
        }
        if (model !== undefined) {
            queryParameters.push("model="+encodeURIComponent(String(model)));
        }

        headers['Accept'] = 'application/json';

        const response: Observable<HttpResponse<object>> = this.httpClient.post(`${this.basePath}/text/text/word-alignment/?${queryParameters.join('&')}`, headers);
        if (observe == 'body') {
               return response.map(httpResponse => <object>(httpResponse.response));
        }
        return response;
    }


    /**
     * Get list of models available for word-alignment
     * 
     
     */
    public getVersionsTextTextWordAlignmentGet(observe?: 'body', headers?: Headers): Observable<object>;
    public getVersionsTextTextWordAlignmentGet(observe?: 'response', headers?: Headers): Observable<HttpResponse<object>>;
    public getVersionsTextTextWordAlignmentGet(observe: any = 'body', headers: Headers = {}): Observable<any> {
        headers['Accept'] = 'application/json';

        const response: Observable<HttpResponse<object>> = this.httpClient.get(`${this.basePath}/text/text/word-alignment/`, headers);
        if (observe == 'body') {
               return response.map(httpResponse => <object>(httpResponse.response));
        }
        return response;
    }

}