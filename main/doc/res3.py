PREFIX asd: <http://example.org/asd#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>

CONSTRUCT {
  ?subject ?predicate ?object .
}
WHERE {
  ?subject ?predicate ?object .
  FILTER (?subject != owl:Thing && ?object != owl:Thing && ?subject != owl:Class && ?object != owl:Class)
}



======

PREFIX asd: <http://example.org/asd#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>

SELECT ?subject ?predicate ?object
WHERE {
  ?subject ?predicate ?object .
  FILTER (?subject != owl:Thing && ?object != owl:Thing && ?subject != owl:Class && ?object != owl:Class)
}


=======

PREFIX asd: <http://example.org/asd#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

CONSTRUCT {
  ?subject ?predicate ?object .
}
WHERE {
  ?subject ?predicate ?object .
  FILTER (
    ?subject != owl:Thing &&
    ?object != owl:Thing &&
    ?subject != owl:Class &&
    ?object != owl:Class
  )
  FILTER NOT EXISTS { ?subject a rdf:Property . }
  FILTER NOT EXISTS { ?object a rdf:Property . }
}


===========

PREFIX asd: <http://example.org/asd#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>

CONSTRUCT {
  ?subject ?predicate ?object .
}
WHERE {
  ?subject ?predicate ?object .
  FILTER (
    ?subject != owl:Thing &&
    ?object != owl:Thing &&
    ?subject != owl:Class &&
    ?object != owl:Class &&
    ?subject != asd:precedes &&
    ?object != asd:precedes
  )
}
