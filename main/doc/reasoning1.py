# Using Stardog Studio to Demonstrate OWL Reasoning: A Step-by-Step Guide

## Introduction

This guide provides comprehensive instructions on how to use Stardog Studio to demonstrate OWL reasoning with a simple example. We will create a model (ontology), insert data, execute queries with and without reasoning, and visualize the results to observe the effects of inference.

## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Setting Up Stardog Studio](#setting-up-stardog-studio)
3. [Creating a Database](#creating-a-database)
4. [Defining the Model (Schema)](#defining-the-model-schema)
5. [Inserting Data](#inserting-data)
6. [Querying Without Reasoning](#querying-without-reasoning)
7. [Enabling Reasoning and Querying with Reasoning](#enabling-reasoning-and-querying-with-reasoning)
8. [Visualizing the Results](#visualizing-the-results)
9. [Comparing Results with and Without Reasoning](#comparing-results-with-and-without-reasoning)
10. [Conclusion](#conclusion)

---

## Prerequisites

- **Stardog and Stardog Studio Installed**: Ensure you have Stardog and Stardog Studio installed on your system.
- **Basic Understanding of RDF, OWL, and SPARQL**: Familiarity with these concepts will help you follow along.

---

## Setting Up Stardog Studio

1. **Launch Stardog Studio**: Open Stardog Studio on your computer.
2. **Connect to Stardog Server**:
   - If not already connected, click on **"Add Connection"**.
   - Enter your **server URL** (e.g., `http://localhost:5820`), **username**, and **password**.
   - Click **"Connect"**.

---

## Creating a Database

1. **Create a New Database**:
   - Click on **"Databases"** in the left sidebar.
   - Click on **"Create Database"**.
2. **Configure Database Settings**:
   - **Database Name**: Enter `myDatabase`.
   - **Advanced Settings**:
     - **Reasoning**:
       - Ensure that **"Enable Reasoning"** is checked.
       - Set **Reasoning Type** to `SL` (Standard Logic) or leave it as default.
     - **Reasoning Schema Graphs**:
       - By default, Stardog uses `<tag:stardog:api:context:schema>` as the reasoning schema graph.
   - Click **"Create"**.

---

## Defining the Model (Schema)

We will define a simple ontology with an `event` class and a `precedes` property, which is transitive.

1. **Open a New Query Tab**:
   - Click on **"New Query"** in the top toolbar.
2. **Insert the Schema into the Reasoning Schema Graph**:
   - **SPARQL Update Query**:

     ```sparql
     PREFIX asd: <http://example.org/asd#>
     PREFIX owl: <http://www.w3.org/2002/07/owl#>
     PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

     INSERT DATA {
       GRAPH <tag:stardog:api:context:schema> {
         asd:event a owl:Class ;
             rdfs:label "event" .

         asd:precedes a owl:ObjectProperty, owl:TransitiveProperty ;
             rdfs:label "precedes" .
       }
     }
     ```

   - **Instructions**:
     - Paste the above query into the query editor.
     - Ensure the **query type** is set to **"Update"**.
     - Click **"Run"** to execute the query.

**Note**: By inserting the schema into `<tag:stardog:api:context:schema>`, we ensure that Stardog uses it for reasoning.

---

## Inserting Data

Next, we'll add instances of `asd:event` and define relationships using `asd:precedes`.

1. **Insert the Data into the Default Graph**:
   - **SPARQL Update Query**:

     ```sparql
     PREFIX asd: <http://example.org/asd#>

     INSERT DATA {
       asd:e1 a asd:event .
       asd:e2 a asd:event .
       asd:e3 a asd:event .

       asd:e1 asd:precedes asd:e2 .
       asd:e2 asd:precedes asd:e3 .
     }
     ```

   - **Instructions**:
     - Open a new query tab or use the same one.
     - Paste the above query into the editor.
     - Ensure the **query type** is set to **"Update"**.
     - Click **"Run"** to execute the query.

---

## Querying Without Reasoning

Let's query the data without reasoning to see only the explicitly asserted relationships.

1. **Write a SPARQL Query**:

   ```sparql
   PREFIX asd: <http://example.org/asd#>

   SELECT ?event1 ?event2
   WHERE {
     ?event1 a asd:event .
     ?event1 asd:precedes ?event2 .
   }
   ```

2. **Execute the Query**:
   - **Instructions**:
     - Open a new query tab.
     - Paste the query into the editor.
     - Ensure that **reasoning is disabled** (the reasoning toggle or lightbulb icon is **off**).
     - Click **"Run"**.
   - **Expected Results**:

     | event1 | event2 |
     |--------|--------|
     | asd:e1 | asd:e2 |
     | asd:e2 | asd:e3 |

---

## Enabling Reasoning and Querying with Reasoning

Now, we'll enable reasoning to see inferred relationships based on the transitive property.

1. **Enable Reasoning**:
   - Toggle the **reasoning option** on (the lightbulb icon is **active**).
2. **Execute the Same Query**:
   - Click **"Run"**.
3. **Expected Results with Reasoning**:

   | event1 | event2 |
   |--------|--------|
   | asd:e1 | asd:e2 |
   | asd:e2 | asd:e3 |
   | **asd:e1** | **asd:e3** | *(Inferred due to transitivity)*

   - The additional row `(asd:e1, asd:e3)` is inferred.

---

## Visualizing the Results

To better understand the impact of reasoning, we'll visualize the graph.

### Visualizing Without Reasoning

1. **Use a CONSTRUCT Query**:

   ```sparql
   PREFIX asd: <http://example.org/asd#>

   CONSTRUCT {
     ?event1 asd:precedes ?event2 .
   }
   WHERE {
     ?event1 a asd:event .
     ?event1 asd:precedes ?event2 .
   }
   ```

2. **Execute the Query Without Reasoning**:
   - Ensure **reasoning is disabled**.
   - Click **"Run"**.
3. **Visualize the Graph**:
   - Switch to the **"Graph"** view in Stardog Studio.
   - You should see two edges:
     - `asd:e1` precedes `asd:e2`
     - `asd:e2` precedes `asd:e3`

### Visualizing With Reasoning

1. **Enable Reasoning**:
   - Toggle reasoning **on**.
2. **Execute the Same CONSTRUCT Query**:
   - Click **"Run"**.
3. **Visualize the Graph**:
   - The graph now includes an additional edge:
     - `asd:e1` precedes `asd:e3` *(inferred)*

### Differentiating Inferred Edges

To clearly see which edges are inferred, we'll modify the CONSTRUCT query.

1. **Modified CONSTRUCT Query**:

   ```sparql
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
       GRAPH <tag:stardog:api:context:default> {
         ?event1 asd:precedes ?event2 .
       }
       BIND("asserted" AS ?edgeType)
       BIND(IRI(CONCAT("urn:edge:", STRUUID())) AS ?edge)
     }
     UNION
     {
       GRAPH <tag:stardog:api:context:inference> {
         ?event1 asd:precedes ?event2 .
       }
       FILTER NOT EXISTS {
         GRAPH <tag:stardog:api:context:default> {
           ?event1 asd:precedes ?event2 .
         }
       }
       BIND("inferred" AS ?edgeType)
       BIND(IRI(CONCAT("urn:edge:", STRUUID())) AS ?edge)
     }
   }
   ```

   - **Explanation**:
     - We retrieve asserted edges from the default graph.
     - We retrieve inferred edges from the inference graph, excluding those already asserted.
     - We label edges as "asserted" or "inferred" using `asd:edgeType`.

2. **Execute the Query with Reasoning Enabled**:
   - Click **"Run"**.
3. **Visualize and Differentiate Edges**:
   - In the **"Graph"** view, use the visualization settings to color-code edges based on `asd:edgeType`:
     - **Asserted Edges**: Blue
     - **Inferred Edges**: Red

---

## Comparing Results with and Without Reasoning

By comparing the visualizations:

- **Without Reasoning**:
  - Only the explicitly asserted edges are visible.
  - Edges:
    - `asd:e1` precedes `asd:e2`
    - `asd:e2` precedes `asd:e3`

- **With Reasoning**:
  - The inferred edge `asd:e1` precedes `asd:e3` is added.
  - Edges:
    - `asd:e1` precedes `asd:e2` *(asserted)*
    - `asd:e2` precedes `asd:e3` *(asserted)*
    - `asd:e1` precedes `asd:e3` *(inferred)*

---

## Conclusion

In this guide, we've:

- Created a simple ontology in Stardog Studio.
- Inserted data and defined relationships.
- Executed queries with and without reasoning to observe the effects of inference.
- Visualized the graph to see the additional edge resulting from reasoning.

By following these steps, you can leverage Stardog's reasoning capabilities to infer new knowledge from your data, enhancing the expressiveness and utility of your semantic models.

---

## Appendix: Full Code Listings

### Schema Insertion Query

```sparql
PREFIX asd: <http://example.org/asd#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

INSERT DATA {
  GRAPH <tag:stardog:api:context:schema> {
    asd:event a owl:Class ;
        rdfs:label "event" .

    asd:precedes a owl:ObjectProperty, owl:TransitiveProperty ;
        rdfs:label "precedes" .
  }
}
```

### Data Insertion Query

```sparql
PREFIX asd: <http://example.org/asd#>

INSERT DATA {
  asd:e1 a asd:event .
  asd:e2 a asd:event .
  asd:e3 a asd:event .

  asd:e1 asd:precedes asd:e2 .
  asd:e2 asd:precedes asd:e3 .
}
```

### Basic Query

```sparql
PREFIX asd: <http://example.org/asd#>

SELECT ?event1 ?event2
WHERE {
  ?event1 a asd:event .
  ?event1 asd:precedes ?event2 .
}
```

### Visualization Query (Differentiated Edges)

```sparql
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
    GRAPH <tag:stardog:api:context:default> {
      ?event1 asd:precedes ?event2 .
    }
    BIND("asserted" AS ?edgeType)
    BIND(IRI(CONCAT("urn:edge:", STRUUID())) AS ?edge)
  }
  UNION
  {
    GRAPH <tag:stardog:api:context:inference> {
      ?event1 asd:precedes ?event2 .
    }
    FILTER NOT EXISTS {
      GRAPH <tag:stardog:api:context:default> {
        ?event1 asd:precedes ?event2 .
      }
    }
    BIND("inferred" AS ?edgeType)
    BIND(IRI(CONCAT("urn:edge:", STRUUID())) AS ?edge)
  }
}
```

---

## Additional Tips

- **Namespaces**: Ensure that the prefixes used (`asd`, `owl`, `rdfs`) are consistently defined in your queries.
- **Reasoning Profiles**: For more complex reasoning tasks, you can explore different reasoning profiles (e.g., `RDFS`, `QL`, `RL`, `EL`).
- **Troubleshooting**:
  - If you don't see inferred results, check that reasoning is enabled and that your schema is correctly inserted into the reasoning schema graph.
  - Verify that your property definitions (e.g., `owl:TransitiveProperty`) are accurate.

---

**Feel free to explore further and experiment with more complex ontologies and reasoning capabilities in Stardog Studio!**
