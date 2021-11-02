{-
   FastAPI
   No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

   The version of the OpenAPI document: 0.1.0

   NOTE: This file is auto generated by the openapi-generator.
   https://github.com/openapitools/openapi-generator.git
   Do not edit this file manually.
-}


module Request.TextTextSummarization exposing (applyTextTextSummarizationPost, getVersionsTextTextSummarizationGet)

import Data.HTTPValidationError as HTTPValidationError exposing (HTTPValidationError)
import Data.Object as Object exposing (Object)
import Dict
import Http
import Json.Decode as Decode
import Url.Builder as Url


basePath : String
basePath =
    "http://localhost"


applyTextTextSummarizationPost :
    { onSend : Result Http.Error Object -> msg




    , text : Maybe (String)    , sourceLanguage : Maybe (String)    , maxLength : Maybe (Int)    , minLength : Maybe (Int)    , model : Maybe (String)
    }
    -> Cmd msg
applyTextTextSummarizationPost params =
    Http.request
        { method = "POST"
        , headers = []
        , url = Url.crossOrigin basePath
            ["text", "text", "summarization"]
            (List.filterMap identity [Maybe.map (Url.string "text" ) params.text, Maybe.map (Url.string "source_language" ) params.sourceLanguage, Maybe.map (Url.string "max_length" << String.fromInt) params.maxLength, Maybe.map (Url.string "min_length" << String.fromInt) params.minLength, Maybe.map (Url.string "model" ) params.model])
        , body = Http.emptyBody
        , expect = Http.expectJson params.onSend Object.decoder
        , timeout = Just 30000
        , tracker = Nothing
        }


getVersionsTextTextSummarizationGet :
    { onSend : Result Http.Error Object -> msg





    }
    -> Cmd msg
getVersionsTextTextSummarizationGet params =
    Http.request
        { method = "GET"
        , headers = []
        , url = Url.crossOrigin basePath
            ["text", "text", "summarization"]
            []
        , body = Http.emptyBody
        , expect = Http.expectJson params.onSend Object.decoder
        , timeout = Just 30000
        , tracker = Nothing
        }