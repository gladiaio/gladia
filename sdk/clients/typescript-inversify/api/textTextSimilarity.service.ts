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
export class TextTextSimilarityService {
    private basePath: string = 'http://localhost';

    constructor(@inject("IApiHttpClient") private httpClient: IHttpClient,
        @inject("IAPIConfiguration") private APIConfiguration: IAPIConfiguration ) {
        if(this.APIConfiguration.basePath)
            this.basePath = this.APIConfiguration.basePath;
    }

    /**
     * Apply model for the similarity task for a given models
     * 
     * @param sentence1 
     * @param sentence2 
     * @param model 
     
     */
    public applyTextTextSimilarityPost(sentence1?: string, sentence2?: string, model?: 'all-MiniLM-L6-v2', observe?: 'body', headers?: Headers): Observable<object>;
    public applyTextTextSimilarityPost(sentence1?: string, sentence2?: string, model?: 'all-MiniLM-L6-v2', observe?: 'response', headers?: Headers): Observable<HttpResponse<object>>;
    public applyTextTextSimilarityPost(sentence1?: string, sentence2?: string, model?: 'all-MiniLM-L6-v2', observe: any = 'body', headers: Headers = {}): Observable<any> {
        let queryParameters: string[] = [];
        if (sentence1 !== undefined) {
            queryParameters.push("sentence1="+encodeURIComponent(String(sentence1)));
        }
        if (sentence2 !== undefined) {
            queryParameters.push("sentence2="+encodeURIComponent(String(sentence2)));
        }
        if (model !== undefined) {
            queryParameters.push("model="+encodeURIComponent(String(model)));
        }

        headers['Accept'] = 'application/json';

        const response: Observable<HttpResponse<object>> = this.httpClient.post(`${this.basePath}/text/text/similarity/?${queryParameters.join('&')}`, headers);
        if (observe == 'body') {
               return response.map(httpResponse => <object>(httpResponse.response));
        }
        return response;
    }


    /**
     * Get list of models available for similarity
     * 
     
     */
    public getVersionsTextTextSimilarityGet(observe?: 'body', headers?: Headers): Observable<object>;
    public getVersionsTextTextSimilarityGet(observe?: 'response', headers?: Headers): Observable<HttpResponse<object>>;
    public getVersionsTextTextSimilarityGet(observe: any = 'body', headers: Headers = {}): Observable<any> {
        headers['Accept'] = 'application/json';

        const response: Observable<HttpResponse<object>> = this.httpClient.get(`${this.basePath}/text/text/similarity/`, headers);
        if (observe == 'body') {
               return response.map(httpResponse => <object>(httpResponse.response));
        }
        return response;
    }

}