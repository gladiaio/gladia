/*
 * FastAPI
 *
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 0.1.0
 * 
 * Generated by: https://openapi-generator.tech
 */

use std::rc::Rc;
use std::borrow::Borrow;

use hyper;
use serde_json;
use futures::Future;

use super::{Error, configuration};
use super::request as __internal_request;

pub struct ImageImageBackgroundRemovalApiClient<C: hyper::client::Connect> {
    configuration: Rc<configuration::Configuration<C>>,
}

impl<C: hyper::client::Connect> ImageImageBackgroundRemovalApiClient<C> {
    pub fn new(configuration: Rc<configuration::Configuration<C>>) -> ImageImageBackgroundRemovalApiClient<C> {
        ImageImageBackgroundRemovalApiClient {
            configuration: configuration,
        }
    }
}

pub trait ImageImageBackgroundRemovalApi {
    fn apply_image_image_background_removal_post(&self, image: &std::path::Path, model: &str) -> Box<Future<Item = Value, Error = Error<serde_json::Value>>>;
    fn get_versions_image_image_background_removal_get(&self, ) -> Box<Future<Item = Value, Error = Error<serde_json::Value>>>;
}


impl<C: hyper::client::Connect>ImageImageBackgroundRemovalApi for ImageImageBackgroundRemovalApiClient<C> {
    fn apply_image_image_background_removal_post(&self, image: &std::path::Path, model: &str) -> Box<Future<Item = Value, Error = Error<serde_json::Value>>> {
        __internal_request::Request::new(hyper::Method::Post, "/image/image/background-removal/".to_string())
            .with_query_param("model".to_string(), model.to_string())
            .with_form_param("image".to_string(), unimplemented!())
            .execute(self.configuration.borrow())
    }

    fn get_versions_image_image_background_removal_get(&self, ) -> Box<Future<Item = Value, Error = Error<serde_json::Value>>> {
        __internal_request::Request::new(hyper::Method::Get, "/image/image/background-removal/".to_string())
            .execute(self.configuration.borrow())
    }

}