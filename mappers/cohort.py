# Auto generated from metaCohortModel.yaml by pythongen.py version: 0.0.1
# Generation date: 2024-11-06T16:34:02
# Schema: CohortData
#
# id: http://example.org/CohortData
# description: A model to represent cohort data
# license: https://creativecommons.org/publicdomain/zero/1.0/

import dataclasses
import re
from dataclasses import dataclass
from datetime import (
    date,
    datetime,
    time
)
from typing import (
    Any,
    ClassVar,
    Dict,
    List,
    Optional,
    Union
)

from jsonasobj2 import (
    JsonObj,
    as_dict
)
from linkml_runtime.linkml_model.meta import (
    EnumDefinition,
    PermissibleValue,
    PvFormulaOptions
)
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from linkml_runtime.utils.formatutils import (
    camelcase,
    sfx,
    underscore
)
from linkml_runtime.utils.metamodelcore import (
    bnode,
    empty_dict,
    empty_list
)
from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.yamlutils import (
    YAMLRoot,
    extended_float,
    extended_int,
    extended_str
)
from rdflib import (
    Namespace,
    URIRef
)

from linkml_runtime.linkml_model.types import Integer, String

metamodel_version = "1.7.0"
version = None

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
PATO = CurieNamespace('PATO', 'http://purl.obolibrary.org/obo/PATO_')
EX = CurieNamespace('ex', 'http://example.org/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
DEFAULT_ = EX


# Types

# Class references



@dataclass(repr=False)
class CohortData(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EX["CohortData"]
    class_class_curie: ClassVar[str] = "ex:CohortData"
    class_name: ClassVar[str] = "CohortData"
    class_model_uri: ClassVar[URIRef] = EX.CohortData

    subjects: Optional[Union[Union[dict, "Subject"], List[Union[dict, "Subject"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        self._normalize_inlined_as_dict(slot_name="subjects", slot_type=Subject, key_name="sex", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Subject(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EX["Subject"]
    class_class_curie: ClassVar[str] = "ex:Subject"
    class_name: ClassVar[str] = "Subject"
    class_model_uri: ClassVar[URIRef] = EX.Subject

    sex: str = None
    age: Optional[int] = None
    disease: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.sex):
            self.MissingRequiredField("sex")
        if not isinstance(self.sex, str):
            self.sex = str(self.sex)

        if self.age is not None and not isinstance(self.age, int):
            self.age = int(self.age)

        if self.disease is not None and not isinstance(self.disease, str):
            self.disease = str(self.disease)

        super().__post_init__(**kwargs)


# Enumerations
class SexEnum(EnumDefinitionImpl):

    FEMALE = PermissibleValue(
        text="FEMALE",
        meaning=PATO["0000383"])
    MALE = PermissibleValue(
        text="MALE",
        meaning=PATO["0000384"])
    UNKNOWN = PermissibleValue(text="UNKNOWN")

    _defn = EnumDefinition(
        name="SexEnum",
    )

# Slots
class slots:
    pass

slots.subjects = Slot(uri=EX.subjects, name="subjects", curie=EX.curie('subjects'),
                   model_uri=EX.subjects, domain=None, range=Optional[str])

slots.sex = Slot(uri=EX.sex, name="sex", curie=EX.curie('sex'),
                   model_uri=EX.sex, domain=None, range=Optional[Union[str, "SexEnum"]])

slots.age = Slot(uri=EX.age, name="age", curie=EX.curie('age'),
                   model_uri=EX.age, domain=None, range=Optional[str])

slots.disease = Slot(uri=EX.disease, name="disease", curie=EX.curie('disease'),
                   model_uri=EX.disease, domain=None, range=Optional[str])

slots.cohortData__subjects = Slot(uri=EX.subjects, name="cohortData__subjects", curie=EX.curie('subjects'),
                   model_uri=EX.cohortData__subjects, domain=None, range=Optional[Union[Union[dict, Subject], List[Union[dict, Subject]]]])

slots.subject__sex = Slot(uri=EX.sex, name="subject__sex", curie=EX.curie('sex'),
                   model_uri=EX.subject__sex, domain=None, range=str)

slots.subject__age = Slot(uri=EX.age, name="subject__age", curie=EX.curie('age'),
                   model_uri=EX.subject__age, domain=None, range=Optional[int])

slots.subject__disease = Slot(uri=EX.disease, name="subject__disease", curie=EX.curie('disease'),
                   model_uri=EX.subject__disease, domain=None, range=Optional[str])
