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
export class TextTextAutocorrectService {
    private basePath: string = 'http://localhost';

    constructor(@inject("IApiHttpClient") private httpClient: IHttpClient,
        @inject("IAPIConfiguration") private APIConfiguration: IAPIConfiguration ) {
        if(this.APIConfiguration.basePath)
            this.basePath = this.APIConfiguration.basePath;
    }

    /**
     * Apply model for the autocorrect task for a given models
     * 
     * @param sentence 
     * @param model 
     
     */
    public applyTextTextAutocorrectPost(sentence?: string, model?: 'flexudy-t5-base-multi-sentence-doctor', observe?: 'body', headers?: Headers): Observable<object>;
    public applyTextTextAutocorrectPost(sentence?: string, model?: 'flexudy-t5-base-multi-sentence-doctor', observe?: 'response', headers?: Headers): Observable<HttpResponse<object>>;
    public applyTextTextAutocorrectPost(sentence?: string, model?: 'flexudy-t5-base-multi-sentence-doctor', observe: any = 'body', headers: Headers = {}): Observable<any> {
        let queryParameters: string[] = [];
        if (sentence !== undefined) {
            queryParameters.push("sentence="+encodeURIComponent(String(sentence)));
        }
        if (model !== undefined) {
            queryParameters.push("model="+encodeURIComponent(String(model)));
        }

        headers['Accept'] = 'application/json';

        const response: Observable<HttpResponse<object>> = this.httpClient.post(`${this.basePath}/text/text/autocorrect/?${queryParameters.join('&')}`, headers);
        if (observe == 'body') {
               return response.map(httpResponse => <object>(httpResponse.response));
        }
        return response;
    }


    /**
     * Get list of models available for autocorrect
     * 
     
     */
    public getVersionsTextTextAutocorrectGet(observe?: 'body', headers?: Headers): Observable<object>;
    public getVersionsTextTextAutocorrectGet(observe?: 'response', headers?: Headers): Observable<HttpResponse<object>>;
    public getVersionsTextTextAutocorrectGet(observe: any = 'body', headers: Headers = {}): Observable<any> {
        headers['Accept'] = 'application/json';

        const response: Observable<HttpResponse<object>> = this.httpClient.get(`${this.basePath}/text/text/autocorrect/`, headers);
        if (observe == 'body') {
               return response.map(httpResponse => <object>(httpResponse.response));
        }
        return response;
    }

}