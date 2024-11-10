@prefix : <http://api.stardog.com/> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix so: <https://schema.org/> .
@prefix stardog: <tag:stardog:api:> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
@prefix asd: <tag:stardog:studio:asd:model:> .

asd:event a owl:Class ;
    rdfs:label "event" ;
    <tag:stardog:studio:label> "event" .

asd:precedes a owl:ObjectProperty , owl:TransitiveProperty ;
    rdfs:label "precedes" ;
    <tag:stardog:studio:label> "precedes" .

asd:e1 a asd:event ;
    asd:precedes asd:e2 .

asd:e2 a asd:event ;
    asd:precedes asd:e3 .

asd:e3 a asd:event .
