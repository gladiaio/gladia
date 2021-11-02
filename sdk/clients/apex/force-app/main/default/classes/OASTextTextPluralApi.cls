/*
 * FastAPI
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 0.1.0
 * 
 *
 * NOTE: This class is auto generated by the OAS code generator program.
 * https://github.com/OAS-api/OAS-codegen.git
 * Do not edit the class manually.
 */

public class OASTextTextPluralApi {
    OASClient client;

    public OASTextTextPluralApi(OASClient client) {
        this.client = client;
    }

    public OASTextTextPluralApi() {
        this.client = new OASClient();
    }

    public OASClient getClient() {
        return this.client;
    }

    /**
     * Apply model for the plural task for a given models
     * 
     * @param word  (optional, default to 'cat')
     * @param count  (optional, default to 2)
     * @param model  (optional, default to inflect)
     * @return Object
     * @throws OAS.ApiException if fails to make API call
     */
    public Object applyTextTextPluralPost(Map<String, Object> params) {
        List<OAS.Param> query = new List<OAS.Param>();

        // cast query params to verify their expected type
        query.addAll(client.makeParam('word', (String) params.get('word')));
        query.addAll(client.makeParam('count', (Integer) params.get('count')));
        query.addAll(client.makeParam('model', (String) params.get('model')));

        List<OAS.Param> form = new List<OAS.Param>();

        return (Object) client.invoke(
            'POST', '/text/text/plural/', '',
            query, form,
            new Map<String, Object>(),
            new Map<String, Object>(),
            new List<String>{ 'application/json' },
            new List<String>(),
            new List<String>(),
            Object.class
        );
    }
    /**
     * Get list of models available for plural
     * 
     * @return Object
     * @throws OAS.ApiException if fails to make API call
     */
    public Object getVersionsTextTextPluralGet() {
        List<OAS.Param> query = new List<OAS.Param>();
        List<OAS.Param> form = new List<OAS.Param>();

        return (Object) client.invoke(
            'GET', '/text/text/plural/', '',
            query, form,
            new Map<String, Object>(),
            new Map<String, Object>(),
            new List<String>{ 'application/json' },
            new List<String>(),
            new List<String>(),
            Object.class
        );
    }
}