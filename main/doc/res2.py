PREFIX asd: <tag:stardog:studio:asd:model:>

CONSTRUCT {
  ?event1 asd:precedes ?event2 .
  ?edge a asd:Edge ;
        asd:edgeType "asserted" ;
        asd:from ?event1 ;
        asd:to ?event2 .
}
WHERE {
  GRAPH <tag:stardog:api:context:default> {
    ?event1 asd:precedes ?event2 .
  }
  BIND(IRI(CONCAT("urn:edge:", STRUUID())) AS ?edge)
}





================

PREFIX asd: <tag:stardog:studio:asd:model:>

CONSTRUCT {
  ?event1 asd:precedes ?event2 .
  ?edge a asd:Edge ;
        asd:edgeType "inferred" ;
        asd:from ?event1 ;
        asd:to ?event2 .
}
WHERE {
  GRAPH <tag:stardog:api:context:inference> {
    ?event1 asd:precedes ?event2 .
  }
  BIND(IRI(CONCAT("urn:edge:", STRUUID())) AS ?edge)
}



=====================


PREFIX asd: <http://example.org/asd#>

CONSTRUCT {
  ?event1 asd:precedes ?event2 .
  ?edge a asd:Edge ;
        asd:edgeType ?edgeType ;
        asd:from ?event1 ;
        asd:to ?event2 .
}
WHERE {
  {
    # Retrieve all triples with reasoning enabled
    ?event1 asd:precedes ?event2 .
    BIND("all" AS ?type)
  }
  
  BIND(IRI(CONCAT("urn:edge:", STRUUID())) AS ?edge)
  
  # Determine if the triple is asserted or inferred
  OPTIONAL {
    SERVICE <reasoning:off> {
      ?event1 asd:precedes ?event2 .
    }
    BIND("asserted" AS ?type)
  }
  
  BIND(
    IF(?type = "asserted", "asserted", "inferred") AS ?edgeType
  )
}


================


PREFIX asd: <http://example.org/asd#>

CONSTRUCT {
  ?event1 asd:precedes ?event2 .
  ?edge a asd:Edge ;
        asd:edgeType "inferred" ;
        asd:from ?event1 ;
        asd:to ?event2 .
}
WHERE {
  # Retrieve all triples with reasoning enabled
  ?event1 asd:precedes ?event2 .
  
  # Exclude asserted triples
  MINUS {
    SERVICE <reasoning:off> {
      ?event1 asd:precedes ?event2 .
    }
  }
  
  BIND(IRI(CONCAT("urn:edge:", STRUUID())) AS ?edge)
}

=============


PREFIX asd: <http://example.org/asd#>

CONSTRUCT {
  ?event1 asd:precedes ?event2 .
  ?edge a asd:Edge ;
        asd:edgeType ?edgeType ;
        asd:from ?event1 ;
        asd:to ?event2 .
}
WHERE {
  {
    # Retrieve all triples with reasoning enabled
    ?event1 asd:precedes ?event2 .
    BIND("all" AS ?type)
  }
  
  BIND(IRI(CONCAT("urn:edge:", STRUUID())) AS ?edge)
  
  # Determine if the triple is asserted or inferred
  OPTIONAL {
    SERVICE <reasoning:off> {
      ?event1 asd:precedes ?event2 .
    }
    BIND("asserted" AS ?type)
  }
  
  BIND(
    IF(?type = "asserted", "asserted", "inferred") AS ?edgeType
  )
}



=========


PREFIX asd: <http://example.org/asd#>

CONSTRUCT {
  ?event1 asd:precedes ?event2 .
  ?edge a asd:Edge ;
        asd:edgeType "inferred" ;
        asd:from ?event1 ;
        asd:to ?event2 .
}
WHERE {
  # Retrieve all triples with reasoning enabled
  ?event1 asd:precedes ?event2 .
  
  # Exclude asserted triples
  MINUS {
    SERVICE <reasoning:off> {
      ?event1 asd:precedes ?event2 .
    }
  }
  
  BIND(IRI(CONCAT("urn:edge:", STRUUID())) AS ?edge)
}

