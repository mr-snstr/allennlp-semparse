"""
Executors are classes that deterministically transform programs in domain specific languages
into denotations. We have one executor defined for each language-domain pair that we handle.
"""
from allennlp_semparse.parsimonious_languages.executors.sql_executor import SqlExecutor
