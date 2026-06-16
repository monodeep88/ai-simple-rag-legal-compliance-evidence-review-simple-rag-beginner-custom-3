DOMAIN_SUMMARY = 'A practical Legal Compliance Evidence Review Simple RAG - Beginner Custom 3 assistant tailored for Simple RAG workflows.'
USER_PERSONA = 'Operations user who needs source-grounded answers, checklists, and clear next actions.'
STARTER_QUESTIONS = ['What should I know first about Legal Compliance Evidence Review Simple RAG - Beginner Custom 3?', 'What policy or evidence supports the recommended next step?', 'Create a checklist for handling this request.']
WORKFLOW_STEPS = ['Classify the request', 'Retrieve the most relevant source documents', 'Apply domain-specific business rules', 'Return a cited answer with next actions']
BUSINESS_RULES = ['Always cite source documents when retrieved context is used.', 'Escalate unclear, high-risk, or missing-data cases to a human reviewer.', 'Prefer concise next actions over generic advice.']
TOOL_CATALOG = [{'name': 'document_search', 'description': 'Find relevant cited context.'}, {'name': 'checklist', 'description': 'Create an operational checklist.'}, {'name': 'calculator', 'description': 'Run safe arithmetic checks.'}]
