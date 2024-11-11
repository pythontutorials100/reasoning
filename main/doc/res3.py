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
