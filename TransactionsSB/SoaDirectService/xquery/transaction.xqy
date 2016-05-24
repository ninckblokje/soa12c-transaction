xquery version "1.0" encoding "utf-8";

(:: OracleAnnotationVersion "1.0" ::)

declare namespace ns1="http://xmlns.oracle.com/pcbpel/adapter/db/top/TransactionDbAdapter";
(:: import schema at "../Resources/TransactionDbAdapter_table.xsd" ::)


declare function local:func() as element() (:: schema-element(ns1:TransactionCollection) ::) {
    <ns1:TransactionCollection>
      <ns1:Transaction>
        <ns1:componentName>SoaDirectPipeline</ns1:componentName>
        <ns1:compositeName>SoaDirectService</ns1:compositeName>
      </ns1:Transaction>
    </ns1:TransactionCollection>
};

local:func()
