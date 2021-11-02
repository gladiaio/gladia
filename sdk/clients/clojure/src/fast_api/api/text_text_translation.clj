(ns fast-api.api.text-text-translation
  (:require [fast-api.core :refer [call-api check-required-params with-collection-format *api-context*]]
            [clojure.spec.alpha :as s]
            [spec-tools.core :as st]
            [orchestra.core :refer [defn-spec]]
            [fast-api.specs.body-apply-image-image-background-removal--post :refer :all]
            [fast-api.specs.body-apply-image-image-colorization--post :refer :all]
            [fast-api.specs.body-apply-image-image-uncolorization--post :refer :all]
            [fast-api.specs.body-apply-image-image-super-resolution--post :refer :all]
            [fast-api.specs.validation-error :refer :all]
            [fast-api.specs.http-validation-error :refer :all]
            [fast-api.specs.body-apply-image-image-face-bluring--post :refer :all]
            [fast-api.specs.body-apply-image-image-restoration--post :refer :all]
            )
  (:import (java.io File)))


(defn-spec apply-text-text-translation-post-with-http-info any?
  "Apply model for the translation task for a given models"
  ([] (apply-text-text-translation-post-with-http-info nil))
  ([{:keys [input_string source_language target_language model]} (s/map-of keyword? any?)]
   (call-api "/text/text/translation/" :post
             {:path-params   {}
              :header-params {}
              :query-params  {"input_string" input_string "source_language" source_language "target_language" target_language "model" model }
              :form-params   {}
              :content-types []
              :accepts       ["application/json"]
              :auth-names    []})))

(defn-spec apply-text-text-translation-post any?
  "Apply model for the translation task for a given models"
  ([] (apply-text-text-translation-post nil))
  ([optional-params any?]
   (let [res (:data (apply-text-text-translation-post-with-http-info optional-params))]
     (if (:decode-models *api-context*)
        (st/decode any? res st/string-transformer)
        res))))


(defn-spec get-versions-text-text-translation-get-with-http-info any?
  "Get list of models available for translation"
  []
  (call-api "/text/text/translation/" :get
            {:path-params   {}
             :header-params {}
             :query-params  {}
             :form-params   {}
             :content-types []
             :accepts       ["application/json"]
             :auth-names    []}))

(defn-spec get-versions-text-text-translation-get any?
  "Get list of models available for translation"
  []
  (let [res (:data (get-versions-text-text-translation-get-with-http-info))]
    (if (:decode-models *api-context*)
       (st/decode any? res st/string-transformer)
       res)))

