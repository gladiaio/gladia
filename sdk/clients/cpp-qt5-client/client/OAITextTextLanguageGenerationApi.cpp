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

#include "OAITextTextLanguageGenerationApi.h"
#include "OAIHelpers.h"

#include <QJsonArray>
#include <QJsonDocument>

namespace OpenAPI {

OAITextTextLanguageGenerationApi::OAITextTextLanguageGenerationApi() {

}

OAITextTextLanguageGenerationApi::~OAITextTextLanguageGenerationApi() {

}

OAITextTextLanguageGenerationApi::OAITextTextLanguageGenerationApi(QString host, QString basePath) {
    this->host = host;
    this->basePath = basePath;
}

void
OAITextTextLanguageGenerationApi::applyTextTextLanguageGenerationPost(const QString& text, const QString& model) {
    QString fullPath;
    fullPath.append(this->host).append(this->basePath).append("/text/text/language-generation/");
    
    if (fullPath.indexOf("?") > 0)
      fullPath.append("&");
    else
      fullPath.append("?");
    fullPath.append(QUrl::toPercentEncoding("text"))
        .append("=")
        .append(QUrl::toPercentEncoding(::OpenAPI::toStringValue(text)));
    
    if (fullPath.indexOf("?") > 0)
      fullPath.append("&");
    else
      fullPath.append("?");
    fullPath.append(QUrl::toPercentEncoding("model"))
        .append("=")
        .append(QUrl::toPercentEncoding(::OpenAPI::toStringValue(model)));
    
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker();
    OAIHttpRequestInput input(fullPath, "POST");


    foreach(QString key, this->defaultHeaders.keys()) {
        input.headers.insert(key, this->defaultHeaders.value(key));
    }

    connect(worker,
            &OAIHttpRequestWorker::on_execution_finished,
            this,
            &OAITextTextLanguageGenerationApi::applyTextTextLanguageGenerationPostCallback);

    worker->execute(&input);
}

void
OAITextTextLanguageGenerationApi::applyTextTextLanguageGenerationPostCallback(OAIHttpRequestWorker * worker) {
    QString msg;
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type == QNetworkReply::NoError) {
        msg = QString("Success! %1 bytes").arg(worker->response.length());
    }
    else {
        msg = "Error: " + worker->error_str;
    }
    OAIObject output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        emit applyTextTextLanguageGenerationPostSignal(output);
        emit applyTextTextLanguageGenerationPostSignalFull(worker, output);
    } else {
        emit applyTextTextLanguageGenerationPostSignalE(output, error_type, error_str);
        emit applyTextTextLanguageGenerationPostSignalEFull(worker, error_type, error_str);
    }
}

void
OAITextTextLanguageGenerationApi::getVersionsTextTextLanguageGenerationGet() {
    QString fullPath;
    fullPath.append(this->host).append(this->basePath).append("/text/text/language-generation/");
    
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker();
    OAIHttpRequestInput input(fullPath, "GET");


    foreach(QString key, this->defaultHeaders.keys()) {
        input.headers.insert(key, this->defaultHeaders.value(key));
    }

    connect(worker,
            &OAIHttpRequestWorker::on_execution_finished,
            this,
            &OAITextTextLanguageGenerationApi::getVersionsTextTextLanguageGenerationGetCallback);

    worker->execute(&input);
}

void
OAITextTextLanguageGenerationApi::getVersionsTextTextLanguageGenerationGetCallback(OAIHttpRequestWorker * worker) {
    QString msg;
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type == QNetworkReply::NoError) {
        msg = QString("Success! %1 bytes").arg(worker->response.length());
    }
    else {
        msg = "Error: " + worker->error_str;
    }
    OAIObject output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        emit getVersionsTextTextLanguageGenerationGetSignal(output);
        emit getVersionsTextTextLanguageGenerationGetSignalFull(worker, output);
    } else {
        emit getVersionsTextTextLanguageGenerationGetSignalE(output, error_type, error_str);
        emit getVersionsTextTextLanguageGenerationGetSignalEFull(worker, error_type, error_str);
    }
}


}