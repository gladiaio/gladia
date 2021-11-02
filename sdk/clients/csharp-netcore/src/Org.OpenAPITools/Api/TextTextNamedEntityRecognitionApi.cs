/* 
 * FastAPI
 *
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 0.1.0
 * 
 * Generated by: https://github.com/openapitools/openapi-generator.git
 */


using System;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.Linq;
using System.Net;
using System.Net.Mime;
using Org.OpenAPITools.Client;
using Org.OpenAPITools.Model;

namespace Org.OpenAPITools.Api
{

    /// <summary>
    /// Represents a collection of functions to interact with the API endpoints
    /// </summary>
    public interface ITextTextNamedEntityRecognitionApiSync : IApiAccessor
    {
        #region Synchronous Operations
        /// <summary>
        /// Apply model for the named-entity-recognition task for a given models
        /// </summary>
        /// <remarks>
        /// 
        /// </remarks>
        /// <exception cref="Org.OpenAPITools.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="text"> (optional, default to &quot;Hugging Face Inc. is a company based in New York City. Its headquarters are in DUMBO, therefore very close to the Manhattan Bridge.&quot;)</param>
        /// <param name="model"> (optional, default to dbmdz-bert-large-cased-finetuned-conll03-english)</param>
        /// <returns>Object</returns>
        Object ApplyTextTextNamedEntityRecognitionPost (string text = null, string model = null);

        /// <summary>
        /// Apply model for the named-entity-recognition task for a given models
        /// </summary>
        /// <remarks>
        /// 
        /// </remarks>
        /// <exception cref="Org.OpenAPITools.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="text"> (optional, default to &quot;Hugging Face Inc. is a company based in New York City. Its headquarters are in DUMBO, therefore very close to the Manhattan Bridge.&quot;)</param>
        /// <param name="model"> (optional, default to dbmdz-bert-large-cased-finetuned-conll03-english)</param>
        /// <returns>ApiResponse of Object</returns>
        ApiResponse<Object> ApplyTextTextNamedEntityRecognitionPostWithHttpInfo (string text = null, string model = null);
        /// <summary>
        /// Get list of models available for named-entity-recognition
        /// </summary>
        /// <remarks>
        /// 
        /// </remarks>
        /// <exception cref="Org.OpenAPITools.Client.ApiException">Thrown when fails to make API call</exception>
        /// <returns>Object</returns>
        Object GetVersionsTextTextNamedEntityRecognitionGet ();

        /// <summary>
        /// Get list of models available for named-entity-recognition
        /// </summary>
        /// <remarks>
        /// 
        /// </remarks>
        /// <exception cref="Org.OpenAPITools.Client.ApiException">Thrown when fails to make API call</exception>
        /// <returns>ApiResponse of Object</returns>
        ApiResponse<Object> GetVersionsTextTextNamedEntityRecognitionGetWithHttpInfo ();
        #endregion Synchronous Operations
    }

    /// <summary>
    /// Represents a collection of functions to interact with the API endpoints
    /// </summary>
    public interface ITextTextNamedEntityRecognitionApiAsync : IApiAccessor
    {
        #region Asynchronous Operations
        /// <summary>
        /// Apply model for the named-entity-recognition task for a given models
        /// </summary>
        /// <remarks>
        /// 
        /// </remarks>
        /// <exception cref="Org.OpenAPITools.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="text"> (optional, default to &quot;Hugging Face Inc. is a company based in New York City. Its headquarters are in DUMBO, therefore very close to the Manhattan Bridge.&quot;)</param>
        /// <param name="model"> (optional, default to dbmdz-bert-large-cased-finetuned-conll03-english)</param>
        /// <returns>Task of Object</returns>
        System.Threading.Tasks.Task<Object> ApplyTextTextNamedEntityRecognitionPostAsync (string text = null, string model = null);

        /// <summary>
        /// Apply model for the named-entity-recognition task for a given models
        /// </summary>
        /// <remarks>
        /// 
        /// </remarks>
        /// <exception cref="Org.OpenAPITools.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="text"> (optional, default to &quot;Hugging Face Inc. is a company based in New York City. Its headquarters are in DUMBO, therefore very close to the Manhattan Bridge.&quot;)</param>
        /// <param name="model"> (optional, default to dbmdz-bert-large-cased-finetuned-conll03-english)</param>
        /// <returns>Task of ApiResponse (Object)</returns>
        System.Threading.Tasks.Task<ApiResponse<Object>> ApplyTextTextNamedEntityRecognitionPostAsyncWithHttpInfo (string text = null, string model = null);
        /// <summary>
        /// Get list of models available for named-entity-recognition
        /// </summary>
        /// <remarks>
        /// 
        /// </remarks>
        /// <exception cref="Org.OpenAPITools.Client.ApiException">Thrown when fails to make API call</exception>
        /// <returns>Task of Object</returns>
        System.Threading.Tasks.Task<Object> GetVersionsTextTextNamedEntityRecognitionGetAsync ();

        /// <summary>
        /// Get list of models available for named-entity-recognition
        /// </summary>
        /// <remarks>
        /// 
        /// </remarks>
        /// <exception cref="Org.OpenAPITools.Client.ApiException">Thrown when fails to make API call</exception>
        /// <returns>Task of ApiResponse (Object)</returns>
        System.Threading.Tasks.Task<ApiResponse<Object>> GetVersionsTextTextNamedEntityRecognitionGetAsyncWithHttpInfo ();
        #endregion Asynchronous Operations
    }

    /// <summary>
    /// Represents a collection of functions to interact with the API endpoints
    /// </summary>
    public interface ITextTextNamedEntityRecognitionApi : ITextTextNamedEntityRecognitionApiSync, ITextTextNamedEntityRecognitionApiAsync
    {

    }

    /// <summary>
    /// Represents a collection of functions to interact with the API endpoints
    /// </summary>
    public partial class TextTextNamedEntityRecognitionApi : ITextTextNamedEntityRecognitionApi
    {
        private Org.OpenAPITools.Client.ExceptionFactory _exceptionFactory = (name, response) => null;

        /// <summary>
        /// Initializes a new instance of the <see cref="TextTextNamedEntityRecognitionApi"/> class.
        /// </summary>
        /// <returns></returns>
        public TextTextNamedEntityRecognitionApi() : this((string) null)
        {
        }

        /// <summary>
        /// Initializes a new instance of the <see cref="TextTextNamedEntityRecognitionApi"/> class.
        /// </summary>
        /// <returns></returns>
        public TextTextNamedEntityRecognitionApi(String basePath)
        {
            this.Configuration = Org.OpenAPITools.Client.Configuration.MergeConfigurations(
                Org.OpenAPITools.Client.GlobalConfiguration.Instance,
                new Org.OpenAPITools.Client.Configuration { BasePath = basePath }
            );
            this.Client = new Org.OpenAPITools.Client.ApiClient(this.Configuration.BasePath);
            this.AsynchronousClient = new Org.OpenAPITools.Client.ApiClient(this.Configuration.BasePath);
            this.ExceptionFactory = Org.OpenAPITools.Client.Configuration.DefaultExceptionFactory;
        }

        /// <summary>
        /// Initializes a new instance of the <see cref="TextTextNamedEntityRecognitionApi"/> class
        /// using Configuration object
        /// </summary>
        /// <param name="configuration">An instance of Configuration</param>
        /// <returns></returns>
        public TextTextNamedEntityRecognitionApi(Org.OpenAPITools.Client.Configuration configuration)
        {
            if (configuration == null) throw new ArgumentNullException("configuration");

            this.Configuration = Org.OpenAPITools.Client.Configuration.MergeConfigurations(
                Org.OpenAPITools.Client.GlobalConfiguration.Instance,
                configuration
            );
            this.Client = new Org.OpenAPITools.Client.ApiClient(this.Configuration.BasePath);
            this.AsynchronousClient = new Org.OpenAPITools.Client.ApiClient(this.Configuration.BasePath);
            ExceptionFactory = Org.OpenAPITools.Client.Configuration.DefaultExceptionFactory;
        }

        /// <summary>
        /// Initializes a new instance of the <see cref="PetApi"/> class
        /// using a Configuration object and client instance.
        /// </summary>
        /// <param name="client">The client interface for synchronous API access.</param>
        /// <param name="asyncClient">The client interface for asynchronous API access.</param>
        /// <param name="configuration">The configuration object.</param>
        public TextTextNamedEntityRecognitionApi(Org.OpenAPITools.Client.ISynchronousClient client,Org.OpenAPITools.Client.IAsynchronousClient asyncClient, Org.OpenAPITools.Client.IReadableConfiguration configuration)
        {
            if(client == null) throw new ArgumentNullException("client");
            if(asyncClient == null) throw new ArgumentNullException("asyncClient");
            if(configuration == null) throw new ArgumentNullException("configuration");

            this.Client = client;
            this.AsynchronousClient = asyncClient;
            this.Configuration = configuration;
            this.ExceptionFactory = Org.OpenAPITools.Client.Configuration.DefaultExceptionFactory;
        }

        /// <summary>
        /// The client for accessing this underlying API asynchronously.
        /// </summary>
        public Org.OpenAPITools.Client.IAsynchronousClient AsynchronousClient { get; set; }

        /// <summary>
        /// The client for accessing this underlying API synchronously.
        /// </summary>
        public Org.OpenAPITools.Client.ISynchronousClient Client { get; set; }

        /// <summary>
        /// Gets the base path of the API client.
        /// </summary>
        /// <value>The base path</value>
        public String GetBasePath()
        {
            return this.Configuration.BasePath;
        }

        /// <summary>
        /// Gets or sets the configuration object
        /// </summary>
        /// <value>An instance of the Configuration</value>
        public Org.OpenAPITools.Client.IReadableConfiguration Configuration {get; set;}

        /// <summary>
        /// Provides a factory method hook for the creation of exceptions.
        /// </summary>
        public Org.OpenAPITools.Client.ExceptionFactory ExceptionFactory
        {
            get
            {
                if (_exceptionFactory != null && _exceptionFactory.GetInvocationList().Length > 1)
                {
                    throw new InvalidOperationException("Multicast delegate for ExceptionFactory is unsupported.");
                }
                return _exceptionFactory;
            }
            set { _exceptionFactory = value; }
        }

        /// <summary>
        /// Apply model for the named-entity-recognition task for a given models 
        /// </summary>
        /// <exception cref="Org.OpenAPITools.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="text"> (optional, default to &quot;Hugging Face Inc. is a company based in New York City. Its headquarters are in DUMBO, therefore very close to the Manhattan Bridge.&quot;)</param>
        /// <param name="model"> (optional, default to dbmdz-bert-large-cased-finetuned-conll03-english)</param>
        /// <returns>Object</returns>
        public Object ApplyTextTextNamedEntityRecognitionPost (string text = null, string model = null)
        {
             Org.OpenAPITools.Client.ApiResponse<Object> localVarResponse = ApplyTextTextNamedEntityRecognitionPostWithHttpInfo(text, model);
             return localVarResponse.Data;
        }

        /// <summary>
        /// Apply model for the named-entity-recognition task for a given models 
        /// </summary>
        /// <exception cref="Org.OpenAPITools.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="text"> (optional, default to &quot;Hugging Face Inc. is a company based in New York City. Its headquarters are in DUMBO, therefore very close to the Manhattan Bridge.&quot;)</param>
        /// <param name="model"> (optional, default to dbmdz-bert-large-cased-finetuned-conll03-english)</param>
        /// <returns>ApiResponse of Object</returns>
        public Org.OpenAPITools.Client.ApiResponse< Object > ApplyTextTextNamedEntityRecognitionPostWithHttpInfo (string text = null, string model = null)
        {
            Org.OpenAPITools.Client.RequestOptions requestOptions = new Org.OpenAPITools.Client.RequestOptions();

            String[] @contentTypes = new String[] {
            };

            // to determine the Accept header
            String[] @accepts = new String[] {
                "application/json"
            };

            var localVarContentType = Org.OpenAPITools.Client.ClientUtils.SelectHeaderContentType(@contentTypes);
            if (localVarContentType != null) requestOptions.HeaderParameters.Add("Content-Type", localVarContentType);

            var localVarAccept = Org.OpenAPITools.Client.ClientUtils.SelectHeaderAccept(@accepts);
            if (localVarAccept != null) requestOptions.HeaderParameters.Add("Accept", localVarAccept);

            if (text != null)
            {
                foreach (var kvp in Org.OpenAPITools.Client.ClientUtils.ParameterToMultiMap("", "text", text))
                {
                    foreach (var value in kvp.Value)
                    {
                        requestOptions.QueryParameters.Add(kvp.Key, value);
                    }
                }
            }
            if (model != null)
            {
                foreach (var kvp in Org.OpenAPITools.Client.ClientUtils.ParameterToMultiMap("", "model", model))
                {
                    foreach (var value in kvp.Value)
                    {
                        requestOptions.QueryParameters.Add(kvp.Key, value);
                    }
                }
            }


            // make the HTTP request

            var response = this.Client.Post< Object >("/text/text/named-entity-recognition/", requestOptions, this.Configuration);

            if (this.ExceptionFactory != null)
            {
                Exception exception = this.ExceptionFactory("ApplyTextTextNamedEntityRecognitionPost", response);
                if (exception != null) throw exception;
            }

            return response;
        }

        /// <summary>
        /// Apply model for the named-entity-recognition task for a given models 
        /// </summary>
        /// <exception cref="Org.OpenAPITools.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="text"> (optional, default to &quot;Hugging Face Inc. is a company based in New York City. Its headquarters are in DUMBO, therefore very close to the Manhattan Bridge.&quot;)</param>
        /// <param name="model"> (optional, default to dbmdz-bert-large-cased-finetuned-conll03-english)</param>
        /// <returns>Task of Object</returns>
        public async System.Threading.Tasks.Task<Object> ApplyTextTextNamedEntityRecognitionPostAsync (string text = null, string model = null)
        {
             Org.OpenAPITools.Client.ApiResponse<Object> localVarResponse = await ApplyTextTextNamedEntityRecognitionPostAsyncWithHttpInfo(text, model);
             return localVarResponse.Data;

        }

        /// <summary>
        /// Apply model for the named-entity-recognition task for a given models 
        /// </summary>
        /// <exception cref="Org.OpenAPITools.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="text"> (optional, default to &quot;Hugging Face Inc. is a company based in New York City. Its headquarters are in DUMBO, therefore very close to the Manhattan Bridge.&quot;)</param>
        /// <param name="model"> (optional, default to dbmdz-bert-large-cased-finetuned-conll03-english)</param>
        /// <returns>Task of ApiResponse (Object)</returns>
        public async System.Threading.Tasks.Task<Org.OpenAPITools.Client.ApiResponse<Object>> ApplyTextTextNamedEntityRecognitionPostAsyncWithHttpInfo (string text = null, string model = null)
        {

            Org.OpenAPITools.Client.RequestOptions requestOptions = new Org.OpenAPITools.Client.RequestOptions();

            String[] @contentTypes = new String[] {
            };

            // to determine the Accept header
            String[] @accepts = new String[] {
                "application/json"
            };
            
            foreach (var contentType in @contentTypes)
                requestOptions.HeaderParameters.Add("Content-Type", contentType);
            
            foreach (var accept in @accepts)
                requestOptions.HeaderParameters.Add("Accept", accept);
            
            if (text != null)
            {
                foreach (var kvp in Org.OpenAPITools.Client.ClientUtils.ParameterToMultiMap("", "text", text))
                {
                    foreach (var value in kvp.Value)
                    {
                        requestOptions.QueryParameters.Add(kvp.Key, value);
                    }
                }
            }
            if (model != null)
            {
                foreach (var kvp in Org.OpenAPITools.Client.ClientUtils.ParameterToMultiMap("", "model", model))
                {
                    foreach (var value in kvp.Value)
                    {
                        requestOptions.QueryParameters.Add(kvp.Key, value);
                    }
                }
            }


            // make the HTTP request

            var response = await this.AsynchronousClient.PostAsync<Object>("/text/text/named-entity-recognition/", requestOptions, this.Configuration);

            if (this.ExceptionFactory != null)
            {
                Exception exception = this.ExceptionFactory("ApplyTextTextNamedEntityRecognitionPost", response);
                if (exception != null) throw exception;
            }

            return response;
        }

        /// <summary>
        /// Get list of models available for named-entity-recognition 
        /// </summary>
        /// <exception cref="Org.OpenAPITools.Client.ApiException">Thrown when fails to make API call</exception>
        /// <returns>Object</returns>
        public Object GetVersionsTextTextNamedEntityRecognitionGet ()
        {
             Org.OpenAPITools.Client.ApiResponse<Object> localVarResponse = GetVersionsTextTextNamedEntityRecognitionGetWithHttpInfo();
             return localVarResponse.Data;
        }

        /// <summary>
        /// Get list of models available for named-entity-recognition 
        /// </summary>
        /// <exception cref="Org.OpenAPITools.Client.ApiException">Thrown when fails to make API call</exception>
        /// <returns>ApiResponse of Object</returns>
        public Org.OpenAPITools.Client.ApiResponse< Object > GetVersionsTextTextNamedEntityRecognitionGetWithHttpInfo ()
        {
            Org.OpenAPITools.Client.RequestOptions requestOptions = new Org.OpenAPITools.Client.RequestOptions();

            String[] @contentTypes = new String[] {
            };

            // to determine the Accept header
            String[] @accepts = new String[] {
                "application/json"
            };

            var localVarContentType = Org.OpenAPITools.Client.ClientUtils.SelectHeaderContentType(@contentTypes);
            if (localVarContentType != null) requestOptions.HeaderParameters.Add("Content-Type", localVarContentType);

            var localVarAccept = Org.OpenAPITools.Client.ClientUtils.SelectHeaderAccept(@accepts);
            if (localVarAccept != null) requestOptions.HeaderParameters.Add("Accept", localVarAccept);



            // make the HTTP request

            var response = this.Client.Get< Object >("/text/text/named-entity-recognition/", requestOptions, this.Configuration);

            if (this.ExceptionFactory != null)
            {
                Exception exception = this.ExceptionFactory("GetVersionsTextTextNamedEntityRecognitionGet", response);
                if (exception != null) throw exception;
            }

            return response;
        }

        /// <summary>
        /// Get list of models available for named-entity-recognition 
        /// </summary>
        /// <exception cref="Org.OpenAPITools.Client.ApiException">Thrown when fails to make API call</exception>
        /// <returns>Task of Object</returns>
        public async System.Threading.Tasks.Task<Object> GetVersionsTextTextNamedEntityRecognitionGetAsync ()
        {
             Org.OpenAPITools.Client.ApiResponse<Object> localVarResponse = await GetVersionsTextTextNamedEntityRecognitionGetAsyncWithHttpInfo();
             return localVarResponse.Data;

        }

        /// <summary>
        /// Get list of models available for named-entity-recognition 
        /// </summary>
        /// <exception cref="Org.OpenAPITools.Client.ApiException">Thrown when fails to make API call</exception>
        /// <returns>Task of ApiResponse (Object)</returns>
        public async System.Threading.Tasks.Task<Org.OpenAPITools.Client.ApiResponse<Object>> GetVersionsTextTextNamedEntityRecognitionGetAsyncWithHttpInfo ()
        {

            Org.OpenAPITools.Client.RequestOptions requestOptions = new Org.OpenAPITools.Client.RequestOptions();

            String[] @contentTypes = new String[] {
            };

            // to determine the Accept header
            String[] @accepts = new String[] {
                "application/json"
            };
            
            foreach (var contentType in @contentTypes)
                requestOptions.HeaderParameters.Add("Content-Type", contentType);
            
            foreach (var accept in @accepts)
                requestOptions.HeaderParameters.Add("Accept", accept);
            


            // make the HTTP request

            var response = await this.AsynchronousClient.GetAsync<Object>("/text/text/named-entity-recognition/", requestOptions, this.Configuration);

            if (this.ExceptionFactory != null)
            {
                Exception exception = this.ExceptionFactory("GetVersionsTextTextNamedEntityRecognitionGet", response);
                if (exception != null) throw exception;
            }

            return response;
        }

    }
}