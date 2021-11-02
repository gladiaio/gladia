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

#include "OAIImageImageColorizationApi.h"
#include "OAIHelpers.h"

#include <QJsonArray>
#include <QJsonDocument>

namespace OpenAPI {

OAIImageImageColorizationApi::OAIImageImageColorizationApi() {

}

OAIImageImageColorizationApi::~OAIImageImageColorizationApi() {

}

OAIImageImageColorizationApi::OAIImageImageColorizationApi(QString host, QString basePath) {
    this->host = host;
    this->basePath = basePath;
}

void
OAIImageImageColorizationApi::applyImageImageColorizationPost(const OAIHttpRequestInputFileElement*& image, const QString& model) {
    QString fullPath;
    fullPath.append(this->host).append(this->basePath).append("/image/image/colorization/");
    
    if (fullPath.indexOf("?") > 0)
      fullPath.append("&");
    else
      fullPath.append("?");
    fullPath.append(QUrl::toPercentEncoding("model"))
        .append("=")
        .append(QUrl::toPercentEncoding(::OpenAPI::toStringValue(model)));
    
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker();
    OAIHttpRequestInput input(fullPath, "POST");
    if (image != nullptr) {
        input.add_file("image", (*image).local_filename, (*image).request_filename, (*image).mime_type);
    }
    

    foreach(QString key, this->defaultHeaders.keys()) {
        input.headers.insert(key, this->defaultHeaders.value(key));
    }

    connect(worker,
            &OAIHttpRequestWorker::on_execution_finished,
            this,
            &OAIImageImageColorizationApi::applyImageImageColorizationPostCallback);

    worker->execute(&input);
}

void
OAIImageImageColorizationApi::applyImageImageColorizationPostCallback(OAIHttpRequestWorker * worker) {
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
        emit applyImageImageColorizationPostSignal(output);
        emit applyImageImageColorizationPostSignalFull(worker, output);
    } else {
        emit applyImageImageColorizationPostSignalE(output, error_type, error_str);
        emit applyImageImageColorizationPostSignalEFull(worker, error_type, error_str);
    }
}

void
OAIImageImageColorizationApi::getVersionsImageImageColorizationGet() {
    QString fullPath;
    fullPath.append(this->host).append(this->basePath).append("/image/image/colorization/");
    
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker();
    OAIHttpRequestInput input(fullPath, "GET");


    foreach(QString key, this->defaultHeaders.keys()) {
        input.headers.insert(key, this->defaultHeaders.value(key));
    }

    connect(worker,
            &OAIHttpRequestWorker::on_execution_finished,
            this,
            &OAIImageImageColorizationApi::getVersionsImageImageColorizationGetCallback);

    worker->execute(&input);
}

void
OAIImageImageColorizationApi::getVersionsImageImageColorizationGetCallback(OAIHttpRequestWorker * worker) {
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
        emit getVersionsImageImageColorizationGetSignal(output);
        emit getVersionsImageImageColorizationGetSignalFull(worker, output);
    } else {
        emit getVersionsImageImageColorizationGetSignalE(output, error_type, error_str);
        emit getVersionsImageImageColorizationGetSignalEFull(worker, error_type, error_str);
    }
}


}