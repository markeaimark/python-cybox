import cybox

import cybox.bindings.cybox_common_types_1_0 as common_binding
#TODO: remove this
from cybox.common.baseobjectattribute import baseobjectattribute
from cybox.bindings.cybox_common_types_1_0 import SimpleHashValueType, HashNameType
from cybox.common.baseobjectattribute import Base_Object_Attribute

class Hash(cybox.Entity):
    TYPE_MD5 = "MD5"
    TYPE_MD6 = "MD6"
    TYPE_SHA1 = "SHA1"
    TYPE_SHA256 = "SHA256"
    TYPE_SSDEEP = "SSDEEP"
    TYPE_OTHER = "Other"

    TYPES = (TYPE_MD5, TYPE_MD6, TYPE_SHA1, TYPE_SHA256, TYPE_SSDEEP,
             TYPE_OTHER)

    # Properties
    @property
    def type_(self):
        return self._type

    @type_.setter
    def type_(self, value):
        if value not in Hash.TYPES:
            raise ValueError("Invalid Hash Type: {0}".format(value))
        self._type = value

    @property
    def simple_hash_value(self):
        return self._simple_hash_value

    @simple_hash_value.setter
    def simple_hash_value(self, value):
        self._simple_hash_value = value

    # Other_Type and FuzzyHashes not yet supported.

    # Import/Export
    def to_obj(self):
        hashobj = common_binding.HashType()
        t = HashNameType(valueOf_=self.type_)
        hashobj.set_Type(t)
        v = SimpleHashValueType(valueOf_=self.simple_hash_value)
        hashobj.set_Simple_Hash_Value(v)

        return hashobj

    def to_dict(self):
        return {
            'type': self.type_,
            'simple_hash_value': self.simple_hash_value,
        }

    @staticmethod
    def from_obj(hash_obj):
        hash_ = Hash()
        hash_.type_ = hash_obj.get_Type().get_valueOf_()
        # Only worry about the value for now.
        hash_.value = hash_obj.get_Simple_Hash_Value().get_valueOf_()
        return hash_

    @staticmethod
    def from_dict(hash_dict):
        hash_ = Hash()
        hash_.type_ = hash_dict.get('type')
        hash_.simple_hash_value = hash_dict.get('simple_hash_value')
        return hash_

    # Conversion
    @classmethod
    def object_from_dict(cls, uri_attributes):
        """Create the URI Object object representation from an input dictionary"""
        return cls.from_dict(uri_attributes).to_obj()

    @classmethod
    def dict_from_object(cls, defined_object):
        """Parse and return a dictionary for an URI Object object"""
        return cls.from_obj(defined_object).to_dict()

#class Hash(object):
#    def __init__(self):
#        pass
#
#    @classmethod
#    def object_from_dict(cls, hash_dict):
#        """Create the Hash object representation from an input dictionary"""
#        hash = common_binding.HashType()
#        for hash_key, hash_value in hash_dict.items():
#            if hash_key == 'type' : hash.set_Type(Base_Object_Attribute.object_from_dict(hash_value))
#            if hash_key == 'other_type' : hash.set_Type(Base_Object_Attribute.object_from_dict(hash_value))
#            if hash_key == 'simple_hash_value' : hash.set_Simple_Hash_Value(Base_Object_Attribute.object_from_dict(hash_value))
#            if hash_key == 'fuzzy_hash_value' : hash.set_Fuzzy_Hash_Value(Base_Object_Attribute.object_from_dict(hash_value))
#            if hash_key == 'fuzzy_hash_structure':
#                for fuzzy_hash_structure_dict in hash_value:
#                    fuzzy_hash_structure_object = common_binding.FuzzyHashStructureType()
#                    for fuzzy_key, fuzzy_value in fuzzy_hash_structure_dict.items():
#                        if fuzzy_key == 'block_size' : fuzzy_hash_structure_object.set_Block_Size(Base_Object_Attribute.object_from_dict(fuzzy_value))
#                        if fuzzy_key == 'block_hash' : 
#                            block_hash_dict = fuzzy_value
#                            block_hash_object = common_binding.FuzzyHashBlockType()
#                            for block_hash_key, block_hash_value in block_hash_dict.items():
#                                if block_hash_key == 'segment_count' : block_hash_object.set_Segment_Count(Base_Object_Attribute.object_from_dict(block_hash_value))
#                                if block_hash_key == 'block_hash_value' :
#                                    hash_value_dict = block_hash_value
#                                    hash_value_object = common_binding.HashValueType()
#                                    for hash_value_key, hash_value_value in hash_value_dict.items():
#                                        if hash_value_key == 'simple_hash_value' : hash_value_object.set_Simple_Hash_Value(Base_Object_Attribute.object_from_dict(hash_value_value))
#                                        if hash_value_key == 'fuzzy_hash_value' : hash_value_object.set_Fuzzy_Hash_Value(Base_Object_Attribute.object_from_dict(hash_value_value))
#                                    if hash_value_object.hasContent_(): block_hash_object.set_Block_Hash_Value(hash_value_object)
#                                if block_hash_key == 'segments' :
#                                    segments_dict = block_hash_value
#                                    segments_object = common_binding.HashSegmentsType()
#                                    for segment in segments_dict:
#                                        hash_segment_object = common_binding.HashSegmentType()
#                                        for segment_key, segment_value in segment.items():
#                                            if segment_key == 'trigger_point' : hash_segment_object.set_Trigger_Point(Base_Object_Attribute.object_from_dict(segment_value))
#                                            if segment_key == 'segment_hash' :
#                                                segment_hash_dict = segment_value
#                                                segment_hash_object = common_binding.HashValueType()
#                                                for segment_hash_key, segment_hash_value in segment_hash_dict.items():
#                                                    if segment_hash_key == 'simple_hash_value' : segment_hash_object.set_Simple_Hash_Value(Base_Object_Attribute.object_from_dict(segment_hash_value))
#                                                    if segment_hash_key == 'fuzzy_hash_value' : segment_hash_object.set_Fuzzy_Hash_Value(Base_Object_Attribute.object_from_dict(segment_hash_value))
#                                                if segment_hash_object.hasContent_(): hash_segment_object.set_Segment_Hash(segment_hash_object)
#                                            if segment_key == 'raw_segment_content' : hash_segment_object.set_Raw_Segment_Content(segment_value)
#                                        if hash_segment_object.hasContent_() : segments_object.add_Segment(hash_segment_object)
#                                    if segments_object.hasContent_() : block_hash_object.set_Segments(segments_object)
#                            if block_hash_object.hasContent_() : fuzzy_hash_structure_object.set_Block_Hash(block_hash_object)
#                    if fuzzy_hash_structure_object.hasContent_() : hash.add_Fuzzy_Hash_Structure(fuzzy_hash_structure_object)
#
#        return hash
#
#    @classmethod
#    def dict_from_object(cls, hash_obj):
#        """Parse and return a dictionary for a Hash object"""
#        pass
