class JobsLocator:
    PAGE_LOCATOR = "div.search-result-container div.content section.listContainer article.jobTuple"

    JOB_TITLE = "div.jobTupleHeader div.info a.title"
    COMPANY_NAME = "div.jobTupleHeader div.info div.mt-7 a.subTitle"
    EXPERIENCE = "div.jobTupleHeader div.info ul.mt-7 li.fleft span.ellipsis"
    SALARY = "div.jobTupleHeader div.info ul.mt-7 li.salary span.ellipsis"
    LOCATION = "div.jobTupleHeader div.info ul.mt-7 li.location span.ellipsis"
    SKILL = "ul.tags"
    JOB_AGE = "div.jobTupleFooter div.grey span.fleft"
    JOB_POSTED_TODAY = "div.jobTupleFooter div.green span.fleft"
    JOB_POSTED_FOR_FUTURE = "div.jobTupleFooter div.yellow span.fleft"

    NEXT_PAGE_LOCATOR = "div.search-result-container div.content section.listContainer div.pagination a.fright"
