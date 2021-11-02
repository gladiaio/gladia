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

#ifndef OAI_OAITextTextNextSentencePredictionApi_H
#define OAI_OAITextTextNextSentencePredictionApi_H

#include "OAIHttpRequest.h"

#include "OAIHTTPValidationError.h"
#include "OAIObject.h"
#include <QString>

#include <QObject>

namespace OpenAPI {

class OAITextTextNextSentencePredictionApi: public QObject {
    Q_OBJECT

public:
    OAITextTextNextSentencePredictionApi();
    OAITextTextNextSentencePredictionApi(QString host, QString basePath);
    ~OAITextTextNextSentencePredictionApi();

    QString host;
    QString basePath;
    QMap<QString, QString> defaultHeaders;

    void applyTextTextNextSentencePredictionPost(const QString& sentence_1, const QString& sentence_2, const QString& model);
    void getVersionsTextTextNextSentencePredictionGet();
    
private:
    void applyTextTextNextSentencePredictionPostCallback (OAIHttpRequestWorker * worker);
    void getVersionsTextTextNextSentencePredictionGetCallback (OAIHttpRequestWorker * worker);
    
signals:
    void applyTextTextNextSentencePredictionPostSignal(OAIObject summary);
    void getVersionsTextTextNextSentencePredictionGetSignal(OAIObject summary);
    
    void applyTextTextNextSentencePredictionPostSignalFull(OAIHttpRequestWorker* worker, OAIObject summary);
    void getVersionsTextTextNextSentencePredictionGetSignalFull(OAIHttpRequestWorker* worker, OAIObject summary);
    
    void applyTextTextNextSentencePredictionPostSignalE(OAIObject summary, QNetworkReply::NetworkError error_type, QString& error_str);
    void getVersionsTextTextNextSentencePredictionGetSignalE(OAIObject summary, QNetworkReply::NetworkError error_type, QString& error_str);
    
    void applyTextTextNextSentencePredictionPostSignalEFull(OAIHttpRequestWorker* worker, QNetworkReply::NetworkError error_type, QString& error_str);
    void getVersionsTextTextNextSentencePredictionGetSignalEFull(OAIHttpRequestWorker* worker, QNetworkReply::NetworkError error_type, QString& error_str);
    
};

}
#endif