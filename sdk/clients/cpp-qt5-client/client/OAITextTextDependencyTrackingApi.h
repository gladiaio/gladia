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

#ifndef OAI_OAITextTextDependencyTrackingApi_H
#define OAI_OAITextTextDependencyTrackingApi_H

#include "OAIHttpRequest.h"

#include "OAIHTTPValidationError.h"
#include "OAIObject.h"
#include <QString>

#include <QObject>

namespace OpenAPI {

class OAITextTextDependencyTrackingApi: public QObject {
    Q_OBJECT

public:
    OAITextTextDependencyTrackingApi();
    OAITextTextDependencyTrackingApi(QString host, QString basePath);
    ~OAITextTextDependencyTrackingApi();

    QString host;
    QString basePath;
    QMap<QString, QString> defaultHeaders;

    void applyTextTextDependencyTrackingPost(const QString& input_string, const QString& model);
    void getVersionsTextTextDependencyTrackingGet();
    
private:
    void applyTextTextDependencyTrackingPostCallback (OAIHttpRequestWorker * worker);
    void getVersionsTextTextDependencyTrackingGetCallback (OAIHttpRequestWorker * worker);
    
signals:
    void applyTextTextDependencyTrackingPostSignal(OAIObject summary);
    void getVersionsTextTextDependencyTrackingGetSignal(OAIObject summary);
    
    void applyTextTextDependencyTrackingPostSignalFull(OAIHttpRequestWorker* worker, OAIObject summary);
    void getVersionsTextTextDependencyTrackingGetSignalFull(OAIHttpRequestWorker* worker, OAIObject summary);
    
    void applyTextTextDependencyTrackingPostSignalE(OAIObject summary, QNetworkReply::NetworkError error_type, QString& error_str);
    void getVersionsTextTextDependencyTrackingGetSignalE(OAIObject summary, QNetworkReply::NetworkError error_type, QString& error_str);
    
    void applyTextTextDependencyTrackingPostSignalEFull(OAIHttpRequestWorker* worker, QNetworkReply::NetworkError error_type, QString& error_str);
    void getVersionsTextTextDependencyTrackingGetSignalEFull(OAIHttpRequestWorker* worker, QNetworkReply::NetworkError error_type, QString& error_str);
    
};

}
#endif