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

#ifndef OAI_OAITextTextNextWordPredictionApi_H
#define OAI_OAITextTextNextWordPredictionApi_H

#include "OAIHttpRequest.h"

#include "OAIHTTPValidationError.h"
#include "OAIObject.h"
#include <QString>

#include <QObject>

namespace OpenAPI {

class OAITextTextNextWordPredictionApi: public QObject {
    Q_OBJECT

public:
    OAITextTextNextWordPredictionApi();
    OAITextTextNextWordPredictionApi(QString host, QString basePath);
    ~OAITextTextNextWordPredictionApi();

    QString host;
    QString basePath;
    QMap<QString, QString> defaultHeaders;

    void applyTextTextNextWordPredictionPost(const QString& sentence, const QString& model);
    void getVersionsTextTextNextWordPredictionGet();
    
private:
    void applyTextTextNextWordPredictionPostCallback (OAIHttpRequestWorker * worker);
    void getVersionsTextTextNextWordPredictionGetCallback (OAIHttpRequestWorker * worker);
    
signals:
    void applyTextTextNextWordPredictionPostSignal(OAIObject summary);
    void getVersionsTextTextNextWordPredictionGetSignal(OAIObject summary);
    
    void applyTextTextNextWordPredictionPostSignalFull(OAIHttpRequestWorker* worker, OAIObject summary);
    void getVersionsTextTextNextWordPredictionGetSignalFull(OAIHttpRequestWorker* worker, OAIObject summary);
    
    void applyTextTextNextWordPredictionPostSignalE(OAIObject summary, QNetworkReply::NetworkError error_type, QString& error_str);
    void getVersionsTextTextNextWordPredictionGetSignalE(OAIObject summary, QNetworkReply::NetworkError error_type, QString& error_str);
    
    void applyTextTextNextWordPredictionPostSignalEFull(OAIHttpRequestWorker* worker, QNetworkReply::NetworkError error_type, QString& error_str);
    void getVersionsTextTextNextWordPredictionGetSignalEFull(OAIHttpRequestWorker* worker, QNetworkReply::NetworkError error_type, QString& error_str);
    
};

}
#endif