"created by anjali"

from design_type.connection.moment_connection import MomentConnection
from utils.common.component import *
# from cad.common_logic import CommonDesignLogic
from Common import *
from utils.common.load import Load
from design_report.reportGenerator_latex import CreateLatex
from Report_functions import *
import logging


class BeamCoverPlate(MomentConnection):

    def __init__(self):
        super(BeamCoverPlate, self).__init__()
        self.design_status = False


    def set_osdaglogger(key):

        """
        Function to set Logger for Tension Module
        """

        # @author Arsil Zunzunia
        global logger
        logger = logging.getLogger('osdag')

        logger.setLevel(logging.DEBUG)
        handler = logging.StreamHandler()
        formatter = logging.Formatter(fmt='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%H:%M:%S')

        handler.setFormatter(formatter)
        logger.addHandler(handler)
        handler = logging.FileHandler('logging_text.log')

        formatter = logging.Formatter(fmt='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%H:%M:%S')
        handler.setFormatter(formatter)
        logger.addHandler(handler)

        if key is not None:
            handler = OurLog(key)
            formatter = logging.Formatter(fmt='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                                          datefmt='%H:%M:%S')
            handler.setFormatter(formatter)
            logger.addHandler(handler)

    def input_values(self, existingvalues={}):

        options_list = []

        if KEY_SECSIZE in existingvalues:
            existingvalue_key_secsize = existingvalues[KEY_SECSIZE]
        else:
            existingvalue_key_secsize = ''

        if KEY_MATERIAL in existingvalues:
            existingvalue_key_mtrl = existingvalues[KEY_MATERIAL]
        else:
            existingvalue_key_mtrl = ''

        if KEY_MOMENT in existingvalues:
            existingvalues_key_moment = existingvalues[KEY_MOMENT]
        else:
            existingvalues_key_moment = ''

        if KEY_SHEAR in existingvalues:
            existingvalue_key_versh = existingvalues[KEY_SHEAR]
        else:
            existingvalue_key_versh = ''

        if KEY_AXIAL in existingvalues:
            existingvalue_key_axial = existingvalues[KEY_AXIAL]
        else:
            existingvalue_key_axial = ''

        if KEY_D in existingvalues:
            existingvalue_key_d = existingvalues[KEY_D]
        else:
            existingvalue_key_d = ''

        if KEY_TYP in existingvalues:
            existingvalue_key_typ = existingvalues[KEY_TYP]
        else:
            existingvalue_key_typ = ''

        if KEY_GRD in existingvalues:
            existingvalue_key_grd = existingvalues[KEY_GRD]
        else:
            existingvalue_key_grd = ''

        if KEY_FLANGEPLATE_PREFERENCES in existingvalues:
            existingvalue_key_fplate_pref = existingvalues[KEY_PLATETHK]
        else:
            existingvalue_key_fplate_pref = ''

        if KEY_FLANGEPLATE_THICKNESS in existingvalues:
            existingvalue_key_fplate_thk = existingvalues[KEY_PLATETHK]
        else:
            existingvalue_key_fplate_thk = ''

        if KEY_WEBPLATE_THICKNESS in existingvalues:
            existingvalue_key_wplate_thk = existingvalues[KEY_PLATETHK]
        else:
            existingvalue_key_wplate_thk = ''

        t16 = (KEY_MODULE, KEY_DISP_BEAMCOVERPLATE, TYPE_MODULE, None, None, True, 'No Validator')
        options_list.append(t16)

        t1 = (None, DISP_TITLE_CM, TYPE_TITLE, None, None, True, 'No Validator')
        options_list.append(t1)

        t4 = (KEY_SECSIZE, KEY_DISP_SECSIZE, TYPE_COMBOBOX, existingvalue_key_secsize, connectdb("Beams"), True, 'No Validator')
        options_list.append(t4)

        t15 = (KEY_IMAGE, None, TYPE_IMAGE, None, None, True, 'No Validator')
        options_list.append(t15)

        t5 = (KEY_MATERIAL, KEY_DISP_MATERIAL, TYPE_COMBOBOX, existingvalue_key_mtrl, VALUES_MATERIAL, True, 'No Validator')
        options_list.append(t5)

        t6 = (None, DISP_TITLE_FSL, TYPE_TITLE, None, None, True, 'No Validator')
        options_list.append(t6)

        t17 = (KEY_MOMENT, KEY_DISP_MOMENT, TYPE_TEXTBOX,existingvalues_key_moment, None, True, 'No Validator')
        options_list.append(t17)

        t7 = (KEY_SHEAR, KEY_DISP_SHEAR, TYPE_TEXTBOX, existingvalue_key_versh, None, True, 'No Validator')
        options_list.append(t7)

        t8 = (KEY_AXIAL, KEY_DISP_AXIAL, TYPE_TEXTBOX, existingvalue_key_axial, None, True, 'No Validator')
        options_list.append(t8)

        t9 = (None, DISP_TITLE_BOLT, TYPE_TITLE, None, None, True, 'No Validator')
        options_list.append(t9)

        t10 = (KEY_D, KEY_DISP_D, TYPE_COMBOBOX_CUSTOMIZED, existingvalue_key_d, VALUES_D, True, 'No Validator')
        options_list.append(t10)

        t11 = (KEY_TYP, KEY_DISP_TYP, TYPE_COMBOBOX, existingvalue_key_typ, VALUES_TYP, True, 'No Validator')
        options_list.append(t11)

        t12 = (KEY_GRD, KEY_DISP_GRD, TYPE_COMBOBOX_CUSTOMIZED, existingvalue_key_grd, VALUES_GRD, True, 'No Validator')
        options_list.append(t12)

        t18 = (None, DISP_TITLE_FLANGESPLICEPLATE, TYPE_TITLE, None, None, True, 'No Validator')
        options_list.append(t18)

        t19 = (KEY_FLANGEPLATE_PREFERENCES, KEY_DISP_FLANGESPLATE_PREFERENCES, TYPE_COMBOBOX, existingvalue_key_fplate_pref, VALUES_FLANGEPLATE_PREFERENCES, True, 'No Validator')
        options_list.append(t19)

        t20 = (KEY_FLANGEPLATE_THICKNESS, KEY_DISP_FLANGESPLATE_THICKNESS, TYPE_COMBOBOX_CUSTOMIZED, existingvalue_key_fplate_thk, VALUES_FLANGEPLATE_THICKNESS, True, 'No Validator')
        options_list.append(t20)

        t21 = (None, DISP_TITLE_WEBSPLICEPLATE, TYPE_TITLE, None, None, True, 'No Validator')
        options_list.append(t21)

        t22 = (KEY_WEBPLATE_THICKNESS, KEY_DISP_WEBPLATE_THICKNESS, TYPE_COMBOBOX_CUSTOMIZED, existingvalue_key_wplate_thk, VALUES_WEBPLATE_THICKNESS, True, 'No Validator')
        options_list.append(t22)

        return options_list

    def customized_input(self):

        list1 = []
        t1 = (KEY_GRD, self.grdval_customized)
        list1.append(t1)
        t3 = (KEY_D, self.diam_bolt_customized)
        list1.append(t3)
        t4 = (KEY_WEBPLATE_THICKNESS, self.plate_thick_customized)
        list1.append(t4)
        t5 = (KEY_FLANGEPLATE_THICKNESS, self.plate_thick_customized)
        list1.append(t5)

        return list1


    def flangespacing(self, flag):

        flangespacing = []

        t21 = (KEY_FLANGE_PITCH, KEY_DISP_FLANGE_PLATE_PITCH, TYPE_TEXTBOX,
               self.flange_plate.pitch_provided )
        flangespacing.append(t21)

        t22 = (KEY_ENDDIST_FLANGE, KEY_DISP_END_DIST_FLANGE, TYPE_TEXTBOX,
               self.flange_plate.end_dist_provided)
        flangespacing.append(t22)

        t23 = (KEY_FLANGE_PLATE_GAUGE, KEY_DISP_FLANGE_PLATE_GAUGE, TYPE_TEXTBOX,
               self.flange_plate.gauge_provided)
        flangespacing.append(t23)

        t24 = (KEY_EDGEDIST_FLANGE, KEY_DISP_EDGEDIST_FLANGE, TYPE_TEXTBOX,
               self.flange_plate.edge_dist_provided )
        flangespacing.append(t24)
        return flangespacing
    #
    def webspacing(self, flag):

        webspacing = []

        t8 = (KEY_WEB_PITCH, KEY_DISP_WEB_PLATE_PITCH, TYPE_TEXTBOX, self.web_plate.pitch_provided if flag else '')
        webspacing.append(t8)

        t9 = (KEY_ENDDIST_W, KEY_DISP_END_DIST_W, TYPE_TEXTBOX,
            self.web_plate.end_dist_provided if flag else '')
        webspacing.append(t9)

        t10 = ( KEY_WEB_GAUGE, KEY_DISP_WEB_PLATE_GAUGE, TYPE_TEXTBOX, self.web_plate.gauge_provided if flag else '')
        webspacing.append(t10)

        t11 = (KEY_EDGEDIST_W, KEY_DISP_EDGEDIST_W, TYPE_TEXTBOX,
               self.web_plate.edge_dist_provided if flag else '')
        webspacing.append(t11)
        return webspacing
    #
    def flangecapacity(self, flag):

        flangecapacity = []

        t30 =(KEY_FLANGE_TEN_CAPACITY,KEY_DISP_FLANGE_TEN_CAPACITY,TYPE_TEXTBOX,
               round(self.section.tension_capacity_flange/1000, 2) if flag else '')
        flangecapacity.append(t30)
        t30 = (KEY_FLANGE_PLATE_TEN_CAP, KEY_DISP_FLANGE_PLATE_TEN_CAP, TYPE_TEXTBOX,
               round(self.flange_plate.tension_capacity_flange_plate / 1000, 2) if flag else '')
        flangecapacity.append(t30)

        # t28 = (KEY_FLANGE_PLATE_MOM_DEMAND, KEY_FLANGE_DISP_PLATE_MOM_DEMAND, TYPE_TEXTBOX,
        #        round(self.flange_plate.moment_demand / 1000000, 2) if flag else '')
        # flangecapacity.append(t28)
        #
        # t29 = (KEY_FLANGE_PLATE_MOM_CAPACITY, KEY_FLANGE_DISP_PLATE_MOM_CAPACITY, TYPE_TEXTBOX,
        #        round(self.flange_plate.moment_capacity/1000, 2) if flag else '')
        # flangecapacity.append( t29)

        return flangecapacity

    def webcapacity(self, flag):

        webcapacity = []
        t30 = (KEY_WEB_TEN_CAPACITY, KEY_DISP_WEB_TEN_CAPACITY, TYPE_TEXTBOX,
               round(self.section.tension_capacity_web / 1000, 2) if flag else '')
        webcapacity.append(t30)
        t30 = (KEY_TEN_CAP_WEB_PLATE, KEY_DISP_TEN_CAP_WEB_PLATE, TYPE_TEXTBOX,
               round(self.web_plate.tension_capacity_web_plate/ 1000, 2) if flag else '')
        webcapacity.append(t30)
        t30 = (KEY_WEBPLATE_SHEAR_CAPACITY, KEY_DISP_WEBPLATE_SHEAR_CAPACITY, TYPE_TEXTBOX,
               round(self.web_plate.shear_capacity_web_plate / 1000, 2) if flag else '')
        webcapacity.append(t30)
        #
        t15 = (KEY_WEB_PLATE_MOM_DEMAND, KEY_WEB_DISP_PLATE_MOM_DEMAND, TYPE_TEXTBOX,
               round(self.web_plate.moment_demand / 1000000, 2) if flag else '')
        webcapacity.append(t15)
        #
        # t16 = (KEY_WEB_PLATE_MOM_CAPACITY, KEY_WEB_DISP_PLATE_MOM_CAPACITY, TYPE_TEXTBOX,
        #        round(self.web_plate.moment_capacity/1000, 2) if flag else '')
        # webcapacity.append(t16)
        return webcapacity

    def boltdetails(self,flag):

        boltdetails = []
        t16 = (KEY_FLANGE_BOLT_LINE, KEY_FLANGE_DISP_BOLT_LINE, TYPE_TEXTBOX,
               (self.flange_plate.bolt_line) if flag else '')
        boltdetails.append(t16)

        t16 = (KEY_FLANGE_BOLTS_ONE_LINE, KEY_FLANGE_DISP_BOLTS_ONE_LINE, TYPE_TEXTBOX,
               (self.flange_plate.bolts_one_line) if flag else '')
        boltdetails.append(t16)

        t16 = (KEY_FLANGE_BOLTS_REQ, KEY_FLANGE_DISP_BOLTS_REQ, TYPE_TEXTBOX,
               (self.flange_plate.bolts_required) if flag else '')
        boltdetails.append(t16)

        t16 = (KEY_WEB_BOLT_LINE, KEY_WEB_DISP_BOLT_LINE, TYPE_TEXTBOX,
               (self.web_plate.bolt_line) if flag else '')
        boltdetails.append(t16)

        t16 = (KEY_WEB_BOLTS_ONE_LINE, KEY_WEB_DISP_BOLTS_ONE_LINE, TYPE_TEXTBOX,
               (self.web_plate.bolts_one_line) if flag else '')
        boltdetails.append(t16)

        t16 = (KEY_WEB_BOLTS_REQ , KEY_WEB_DISP_BOLTS_REQ, TYPE_TEXTBOX,
               (self.web_plate.bolts_required) if flag else '')
        boltdetails.append(t16)

        return  boltdetails

    def Innerplate(self, flag):
        Innerplate = []


        t18 = (KEY_INNERFLANGE_PLATE_HEIGHT, KEY_DISP_INNERFLANGE_PLATE_HEIGHT, TYPE_TEXTBOX,
               self.flange_plate.Innerheight if flag else '')
        Innerplate.append(t18)

        t19 = (KEY_INNERFLANGE_PLATE_LENGTH, KEY_DISP_INNERFLANGE_PLATE_LENGTH, TYPE_TEXTBOX,
            self.flange_plate.Innerlength if flag else '')
        Innerplate.append(t19)

        t20 = (KEY_INNERFLANGEPLATE_THICKNESS, KEY_DISP_INNERFLANGESPLATE_THICKNESS, TYPE_TEXTBOX,
               self.flange_plate.thickness_provided if flag else '')
        Innerplate.append(t20)
        return Innerplate
    def member_capacityoutput(self,flag):
        member_capacityoutput = []
        t29 = (KEY_MEMBER_MOM_CAPACITY, KEY_OUT_DISP_MOMENT_CAPACITY, TYPE_TEXTBOX,
               round(self.section.moment_capacity  / 1000000, 2) if flag else '')
        member_capacityoutput.append(t29)
        t29 = (KEY_MEMBER_SHEAR_CAPACITY, KEY_OUT_DISP_SHEAR_CAPACITY, TYPE_TEXTBOX,
               round(self.shear_capacity1 / 1000, 2) if flag else '')
        member_capacityoutput.append(t29)
        t29 = (KEY_MEMBER_AXIALCAPACITY, KEY_OUT_DISP_AXIAL_CAPACITY, TYPE_TEXTBOX,
               round(self.axial_capacity/ 1000, 2) if flag else '')
        member_capacityoutput.append(t29)
        return member_capacityoutput
    def output_values(self, flag):

        out_list = []

        t1 = (None, DISP_TITLE_BOLT, TYPE_TITLE, None, True)
        out_list.append(t1)

        t2 = (KEY_D, KEY_OUT_DISP_D_PROVIDED, TYPE_TEXTBOX,
              self.bolt.bolt_diameter_provided if flag else '', True)
        out_list.append(t2)

        t3 = (KEY_GRD, KEY_DISP_GRD, TYPE_TEXTBOX,
              self.bolt.bolt_grade_provided if flag else '', True)
        out_list.append(t3)

        t4 = (None, DISP_TITLE_BOLTDETAILS, TYPE_TITLE, None, True)
        out_list.append(t4)

        t21 = (KEY_BOLT_DETAILS, KEY_DISP_BOLT_DETAILS, TYPE_OUT_BUTTON, ['Bolt details', self.boltdetails], True)
        out_list.append(t21)
        t4 = (None, DISP_TITLE_MEMBER_CAPACITY, TYPE_TITLE, None, True)
        out_list.append(t4)
        t21 = (KEY_MEMBER_CAPACITY, KEY_DISP_MEMBER_CAPACITY, TYPE_OUT_BUTTON, ['Member Capacity', self.member_capacityoutput], True)
        out_list.append(t21)

        t4 = (None, DISP_TITLE_WEBSPLICEPLATE, TYPE_TITLE, None, True)
        out_list.append(t4)

        t5 = (KEY_WEB_PLATE_HEIGHT, KEY_DISP_WEB_PLATE_HEIGHT, TYPE_TEXTBOX,
              self.web_plate.height if flag else '', True)
        out_list.append(t5)

        t6 = (KEY_WEB_PLATE_LENGTH, KEY_DISP_WEB_PLATE_LENGTH, TYPE_TEXTBOX,
              self.web_plate.length if flag else '', True)
        out_list.append(t6)

        t7 = (KEY_WEBPLATE_THICKNESS, KEY_DISP_WEBPLATE_THICKNESS, TYPE_TEXTBOX,
              self.web_plate.thickness_provided if flag else '', True)
        out_list.append(t7)

        t21 = (KEY_WEB_SPACING, KEY_DISP_WEB_SPACING, TYPE_OUT_BUTTON, ['Web Spacing Details', self.webspacing], True)
        out_list.append(t21)

        t21 = (KEY_WEB_CAPACITY, KEY_DISP_WEB_CAPACITY, TYPE_OUT_BUTTON, ['Web Capacity', self.webcapacity], True)
        out_list.append(t21)

        t17 = (None, DISP_TITLE_FLANGESPLICEPLATE, TYPE_TITLE, None, True)
        out_list.append(t17)

        t18 = (KEY_FLANGE_PLATE_HEIGHT, KEY_DISP_FLANGE_PLATE_HEIGHT, TYPE_TEXTBOX,
               self.flange_plate.height if flag else '', True)
        out_list.append(t18)

        t19 = (
            KEY_FLANGE_PLATE_LENGTH, KEY_DISP_FLANGE_PLATE_LENGTH, TYPE_TEXTBOX,
            self.flange_plate.length if flag else '', True)
        out_list.append(t19)

        t20 = (KEY_FLANGEPLATE_THICKNESS, KEY_DISP_FLANGESPLATE_THICKNESS, TYPE_TEXTBOX,
               self.flange_plate.thickness_provided if flag else '', True)
        out_list.append(t20)
        t21 = (
        KEY_FLANGE_SPACING, KEY_DISP_FLANGE_SPACING, TYPE_OUT_BUTTON, ['Flange Spacing Details', self.flangespacing], True)
        out_list.append(t21)

        t21 = (
            KEY_FLANGE_CAPACITY, KEY_DISP_FLANGE_CAPACITY, TYPE_OUT_BUTTON, ['Flange Capacity', self.flangecapacity], True)
        out_list.append(t21)


        t21 = (KEY_INNERPLATE, DISP_TITLE_INNERFLANGESPLICEPLATE, TYPE_OUT_BUTTON,
               ['Inner Plate Details (mm)', self.Innerplate], True)
        out_list.append(t21)

        return out_list

    def tab_list(self):

        tabs = []

        t1 = (KEY_DISP_BEAMSEC, TYPE_TAB_1, self.tab_beam_section)
        tabs.append(t1)

        t2 = ("Bolt", TYPE_TAB_2, self.bolt_values)
        tabs.append(t2)

        t3 = ("Weld", TYPE_TAB_2, self.weld_values)
        tabs.append(t3)

        t4 = ("Detailing", TYPE_TAB_2, self.detailing_values)
        tabs.append(t4)

        t5 = ("Design", TYPE_TAB_2, self.design_values)
        tabs.append(t5)

        t6 = ("Connector", TYPE_TAB_2, self.connector_values)
        tabs.append(t6)

        return tabs

    def tab_value_changed(self):

        change_tab = []

        t2 = (KEY_DISP_BEAMSEC, [KEY_SUPTDSEC_MATERIAL], [KEY_SUPTDSEC_FU, KEY_SUPTDSEC_FY], TYPE_TEXTBOX, self.get_fu_fy)
        change_tab.append(t2)

        t3 = ("Connector", [KEY_PLATE_MATERIAL], [KEY_PLATE_FU, KEY_PLATE_FY], TYPE_TEXTBOX, self.get_fu_fy)
        change_tab.append(t3)

        t5 = (KEY_DISP_BEAMSEC, ['Label_1', 'Label_2', 'Label_3', 'Label_4'],
              ['Label_11', 'Label_12', 'Label_13', 'Label_14', 'Label_15', 'Label_16', 'Label_17', 'Label_18',
               'Label_19', 'Label_20'], TYPE_TEXTBOX, self.get_sec_properties)
        change_tab.append(t5)

        return change_tab

    def edit_tabs(self):

        return []

    def list_for_fu_fy_validation(self):

        fu_fy_list = []

        t2 = (KEY_SUPTDSEC_MATERIAL, KEY_SUPTDSEC_FU, KEY_SUPTDSEC_FY)
        fu_fy_list.append(t2)

        t3 = (KEY_PLATE_MATERIAL, KEY_PLATE_FU, KEY_PLATE_FY)
        fu_fy_list.append(t3)

        return fu_fy_list

    def input_dictionary_design_pref(self):
        design_input = []

        t2 = (KEY_DISP_BEAMSEC, TYPE_COMBOBOX, [KEY_SUPTDSEC_MATERIAL])
        design_input.append(t2)

        t2 = (KEY_DISP_BEAMSEC, TYPE_TEXTBOX, [KEY_SUPTDSEC_FU, KEY_SUPTDSEC_FY])
        design_input.append(t2)

        t3 = ("Bolt", TYPE_COMBOBOX, [KEY_DP_BOLT_TYPE, KEY_DP_BOLT_HOLE_TYPE, KEY_DP_BOLT_SLIP_FACTOR])
        design_input.append(t3)

        t3 = ("Bolt", TYPE_TEXTBOX, [KEY_DP_BOLT_MATERIAL_G_O])
        design_input.append(t3)

        t4 = ("Weld", TYPE_COMBOBOX, [KEY_DP_WELD_FAB])
        design_input.append(t4)

        t4 = ("Weld", TYPE_TEXTBOX, [KEY_DP_WELD_MATERIAL_G_O])
        design_input.append(t4)

        t5 = ("Detailing", TYPE_COMBOBOX, [KEY_DP_DETAILING_EDGE_TYPE, KEY_DP_DETAILING_CORROSIVE_INFLUENCES])
        design_input.append(t5)

        t5 = ("Detailing", TYPE_TEXTBOX, [KEY_DP_DETAILING_GAP])
        design_input.append(t5)

        t6 = ("Design", TYPE_COMBOBOX, [KEY_DP_DESIGN_METHOD])
        design_input.append(t6)

        t7 = ("Connector", TYPE_COMBOBOX, [KEY_PLATE_MATERIAL])
        design_input.append(t7)

        return design_input

    def input_dictionary_without_design_pref(self):
        design_input = []
        t1 = (KEY_MATERIAL, [KEY_SUPTDSEC_MATERIAL], 'Input Dock')
        design_input.append(t1)

        t2 = (None, [KEY_DP_BOLT_TYPE, KEY_DP_BOLT_HOLE_TYPE, KEY_DP_BOLT_MATERIAL_G_O, KEY_DP_BOLT_SLIP_FACTOR,
                     KEY_DP_WELD_FAB, KEY_DP_WELD_MATERIAL_G_O, KEY_DP_DETAILING_EDGE_TYPE, KEY_DP_DETAILING_GAP,
                     KEY_DP_DETAILING_CORROSIVE_INFLUENCES, KEY_DP_DESIGN_METHOD, KEY_PLATE_MATERIAL], '')
        design_input.append(t2)

        return design_input

    def refresh_input_dock(self):

        add_buttons = []

        t2 = (KEY_DISP_BEAMSEC, KEY_SECSIZE, TYPE_COMBOBOX, KEY_SUPTDSEC_DESIGNATION, None, None, "Beams")
        add_buttons.append(t2)

        return add_buttons

    def func_for_validation(self, design_dictionary):\

        all_errors = []
        self.design_status = False
        flag = False

        option_list = self.input_values(self)
        missing_fields_list = []
        for option in option_list:
            if option[2] == TYPE_TEXTBOX:
                if design_dictionary[option[0]] == '':
                    missing_fields_list.append(option[1])
            elif option[2] == TYPE_COMBOBOX and option[0] != KEY_CONN:
                val = option[4]
                if design_dictionary[option[0]] == val[0]:
                    missing_fields_list.append(option[1])

        if len(missing_fields_list) > 0:
            error = self.generate_missing_fields_error_string(self, missing_fields_list)
            all_errors.append(error)
            # flag = False
        else:
            flag = True

        if flag:
            self.set_input_values(self, design_dictionary)
        else:
            return all_errors

    def warn_text(self):

        """
        Function to give logger warning when any old value is selected from Column and Beams table.
        """

        # @author Arsil Zunzunia
        global logger
        red_list = red_list_function()
        if self.section.designation in red_list or self.section.designation in red_list:
            logger.warning(
                " : You are using a section (in red color) that is not available in latest version of IS 808")
            logger.info(
                " : You are using a section (in red color) that is not available in latest version of IS 808")



    def generate_missing_fields_error_string(self, missing_fields_list):
        """
        Args:
            missing_fields_list: list of fields that are not selected or entered
        Returns:
            error string that has to be displayed
        """
        # The base string which should be displayed
        information = "Please input the following required field"
        if len(missing_fields_list) > 1:
            # Adds 's' to the above sentence if there are multiple missing input fields
            information += "s"
        information += ": "
        # Loops through the list of the missing fields and adds each field to the above sentence with a comma

        for item in missing_fields_list:
            information = information + item + ", "

        # Removes the last comma
        information = information[:-2]
        information += "."

        return information



    def module_name(self):
        return KEY_DISP_BEAMCOVERPLATE

    def set_input_values(self, design_dictionary):
        super(BeamCoverPlate, self).set_input_values(self, design_dictionary)

        self.module = design_dictionary[KEY_MODULE]
        # self.connectivity = design_dictionary[KEY_CONN]
        self.preference = design_dictionary[KEY_FLANGEPLATE_PREFERENCES]

        self.section = Beam(designation=design_dictionary[KEY_SECSIZE],
                              material_grade=design_dictionary[KEY_MATERIAL])
        print("anjali",design_dictionary[KEY_DP_DETAILING_EDGE_TYPE])
        self.web_bolt = Bolt(grade=design_dictionary[KEY_GRD], diameter=design_dictionary[KEY_D],
                             bolt_type=design_dictionary[KEY_TYP], material_grade=design_dictionary[KEY_MATERIAL],
                             bolt_hole_type=design_dictionary[KEY_DP_BOLT_HOLE_TYPE],
                             edge_type=design_dictionary[KEY_DP_DETAILING_EDGE_TYPE],

                             mu_f=design_dictionary[KEY_DP_BOLT_SLIP_FACTOR],
                             corrosive_influences=design_dictionary[KEY_DP_DETAILING_CORROSIVE_INFLUENCES])


        self.bolt = Bolt(grade=design_dictionary[KEY_GRD], diameter=design_dictionary[KEY_D],
                             bolt_type=design_dictionary[KEY_TYP], material_grade=design_dictionary[KEY_MATERIAL],
                             bolt_hole_type=design_dictionary[KEY_DP_BOLT_HOLE_TYPE],
                             edge_type=design_dictionary[KEY_DP_DETAILING_EDGE_TYPE],
                             mu_f=design_dictionary[KEY_DP_BOLT_SLIP_FACTOR],
                             corrosive_influences=design_dictionary[KEY_DP_DETAILING_CORROSIVE_INFLUENCES])
        self.flange_bolt = Bolt(grade=design_dictionary[KEY_GRD], diameter=design_dictionary[KEY_D],
                                bolt_type=design_dictionary[KEY_TYP], material_grade=design_dictionary[KEY_MATERIAL],
                                bolt_hole_type=design_dictionary[KEY_DP_BOLT_HOLE_TYPE],
                                edge_type=design_dictionary[KEY_DP_DETAILING_EDGE_TYPE],
                                mu_f=design_dictionary[KEY_DP_BOLT_SLIP_FACTOR],
                                corrosive_influences=design_dictionary[KEY_DP_DETAILING_CORROSIVE_INFLUENCES])

        self.flange_plate = Plate(thickness=design_dictionary.get(KEY_FLANGEPLATE_THICKNESS, None),
                                  material_grade=design_dictionary[KEY_MATERIAL],
                                  gap=design_dictionary[KEY_DP_DETAILING_GAP])


        self.web_plate = Plate(thickness=design_dictionary.get(KEY_WEBPLATE_THICKNESS, None),
                               material_grade=design_dictionary[KEY_MATERIAL],
                               gap=design_dictionary[KEY_DP_DETAILING_GAP])


        self.member_capacity(self)
        #self.hard_values(self)
    def hard_values(self):
        # Select Selection  WPB 240* 240 * 60.3 (inside Ouside)- material E 250 fe 450A bearing
        #flange bolt
        self.load.moment = 8.318420#kN
        self.factored_axial_load= 481.745#KN
        self.load.shear_force =111.906 # kN
        self.flange_bolt.bolt_type = "Bearing Bolt"
        # self.flange_bolt.bolt_hole_type = bolt_hole_type
        # self.flange_bolt.edge_type = edge_type
        # self.flange_bolt.mu_f = float(mu_f)
        self.flange_bolt.connecting_plates_tk = None

        self.flange_bolt.bolt_grade_provided = 3.6
        self.flange_bolt.bolt_diameter_provided = 24
        self.flange_bolt.dia_hole =26
        # self.flange_bolt.bolt_shear_capacity = 56580.32638058333
        # self.flange_bolt.bolt_bearing_capacity = 118287.48484848486
        # self.flange_bolt.bolt_capacity = 56580.32638058333




        # web bolt
        self.web_bolt.bolt_type = "Bearing Bolt"
        # self.web_bolt.bolt_hole_type = bolt_hole_type
        # self.web_bolt.edge_type = edge_type
        # self.web_bolt.mu_f = float(mu_f)
        self.web_bolt.connecting_plates_tk = None

        self.web_bolt.bolt_grade_provided = 3.6
        self.web_bolt.bolt_diameter_provided = 24
        self.web_bolt.dia_hole = 26
        # self.web_bolt.bolt_shear_capacity = 56580.32638058333
        # self.web_bolt.bolt_bearing_capacity = 69923.63636363638
        # self.web_bolt.bolt_capacity = 69923.63636363638
        # self.web_bolt.min_edge_dist_round = 33
        # self.web_bolt.min_end_dist_round = 33
        # self.web_bolt.min_gauge_round = 50
        #anjali jatav
        # self.web_bolt.min_pitch_round = 50

        # self.web_bolt.max_edge_dist_round = 150
        # self.web_bolt.max_end_dist_round = 150
        # self.web_bolt.max_spacing_round = 300.0

        # self.web_bolt.bolt_shank_area = 0.0
        # self.web_bolt.bolt_net_area = 0.0



        #flange plate
        self.flange_plate.thickness_provided =6
        self.flange_plate.height = 240
        self.flange_plate.length= 310
        self.flange_plate.bolt_line = 4
        self.flange_plate.bolts_one_line =2
        self.flange_plate.bolts_required= 8
        # self.flange_plate.bolt_capacity_red = 56580.32638058333
        # self.flange_plate.bolt_force = 29359.584393928224
        # self.flange_plate.moment_demand= 0
        self.flange_plate.pitch_provided = 60
        self.flange_plate.gauge_provided = 0.0
        self.flange_plate.edge_dist_provided = 45
        self.flange_plate.end_dist_provided= 45

        # web plate
        self.web_plate.thickness_provided = 8
        self.web_plate.height =200
        self.web_plate.length =310
        self.web_plate.bolt_line = 4
        self.web_plate.bolts_one_line = 2
        self.web_plate.bolts_required = 8
        self.web_plate.pitch_provided = 60
        self.web_plate.gauge_provided = 110
        self.web_plate.edge_dist_provided = 45
        self.web_plate.end_dist_provided = 45
        #  Inner Flange plate
        self.flange_plate.thickness_provided = 6
        self.flange_plate.Innerheight = 114.15
        self.flange_plate.Innerlength =310
        self.flange_plate.gap = 10
        self.web_plate.gap = 10

        self.flange_plate.midgauge = 101.7
        self.web_plate.midpitch = 100
        self.flange_plate.midpitch=100
        # self.web_plate.moment_capacity = 0
        self.design_status = True

    def member_capacity(self):
        self.member_capacity_status = False
        if self.section.type == "Rolled":
            length = self.section.depth
        else:
            length = self.section.depth - (
                    2 * self.section.flange_thickness)  # -(2*self.supported_section.root_radius)
        gamma_m0 = 1.1
        ############################# Axial Capacity N ############################
        self.axial_capacity = round((self.section.area * self.section.fy) / gamma_m0, 2)  # N
        self.min_axial_load = 0.3 * self.axial_capacity
        self.factored_axial_load = round(max(self.load.axial_force * 1000, self.min_axial_load), 2)  # N
        print("self.factored_axial_load", self.factored_axial_load)

        ############################# Shear Capacity  # N############################
        self.shear_capacity1 = round(((self.section.depth - (2 * self.section.flange_thickness)) *
                                      self.section.web_thickness * self.section.fy) / (math.sqrt(3) * gamma_m0),
                                     2)  # N # A_v: Total cross sectional area in shear in mm^2 (float)
        self.shear_load1 = 0.6 * self.shear_capacity1  # N
        self.fact_shear_load = round(max(self.shear_load1, self.load.shear_force * 1000), 2)  # N
        print('shear_force', self.load.shear_force)

        # ###########################################################
        # if self.factored_axial_load > self.axial_capacity:
        #     logger.warning(' : Factored axial load is exceeding axial capacity  %2.2f KN' % self.axial_capacity)
        #     self.member_capacity = False
        # else:
        #     if self.fact_shear_load > self.shear_capacity1:
        #         logger.warning(' : Factored shear load is exceeding shear capacity  %2.2f KN' % self.shear_capacity1)
        #         self.member_capacity = False
        #     else:
        #         self.member_capacity = True
        # #############################################################

        self.Z_p = round(((self.section.web_thickness * (
                self.section.depth - 2 * (self.section.flange_thickness)) ** 2) / 4), 2)  # mm3
        self.Z_e = round(((self.section.web_thickness * (
                self.section.depth - 2 * (self.section.flange_thickness)) ** 2) / 6), 2)  # mm3
        # if self.member_capacity == True:
        if self.section.type == "Rolled":
            self.limitwidththkratio_flange = self.limiting_width_thk_ratio(column_f_t=self.section.flange_thickness,
                                                                           column_t_w=self.section.web_thickness,
                                                                           D=self.section.depth,
                                                                           column_b=self.section.flange_width,
                                                                           column_fy=self.section.fy,
                                                                           factored_axial_force=self.factored_axial_load,
                                                                           column_area=self.section.area,
                                                                           compression_element="External",
                                                                           section="Rolled")
        else:
            pass

        if self.section.type2 == "generally":
            self.limitwidththkratio_web = self.limiting_width_thk_ratio(column_f_t=self.section.flange_thickness,
                                                                        column_t_w=self.section.web_thickness,
                                                                        D=self.section.depth,
                                                                        column_b=self.section.flange_width,
                                                                        column_fy=self.section.fy,
                                                                        factored_axial_force=self.factored_axial_load,
                                                                        column_area=self.section.area,
                                                                        compression_element="Web of an I-H",
                                                                        section="generally")
        else:
            pass

        self.class_of_section = int(max(self.limitwidththkratio_flange, self.limitwidththkratio_web))
        if self.class_of_section == 1 or self.class_of_section == 2:
            Z_w = self.Z_p
        elif self.class_of_section == 3:
            Z_w = self.Z_e

        if self.class_of_section == 1 or self.class_of_section == 2:
            self.beta_b = 1
        elif self.class_of_section == 3:
            self.beta_b = self.Z_e / self.Z_p
        ############################ moment_capacty ############################
        self.section.plastic_moment_capacty(beta_b=self.beta_b, Z_p=self.Z_p,
                                            fy=self.section.fy)  # N # for section
        self.section.moment_d_deformation_criteria(fy=self.section.fy, Z_e=self.section.elast_sec_mod_z)
        self.Pmc = self.section.plastic_moment_capactiy
        self.Mdc = self.section.moment_d_def_criteria
        self.section.moment_capacity = round(
            min(self.section.plastic_moment_capactiy, self.section.moment_d_def_criteria), 2)
        self.load_moment_min = 0.5 * self.section.moment_capacity
        self.load_moment = round(max(self.load_moment_min, self.load.moment * 1000000), 2)  # N
        self.moment_web = round((Z_w * self.load_moment / (self.section.plast_sec_mod_z)),
                                2)  # Nm todo add in ddcl # z_w of web & z_p  of section
        self.moment_flange = round(((self.load_moment) - self.moment_web), 2)
        self.axial_force_w = ((self.section.depth - (
                    2 * self.section.flange_thickness)) * self.section.web_thickness * self.factored_axial_load) / (
                                 self.section.area)  # N
        self.axial_force_f = self.factored_axial_load * self.section.flange_width * self.section.flange_thickness / (
            self.section.area)  # N
        self.flange_force = (((self.moment_flange) / (self.section.depth - self.section.flange_thickness)) + (
            self.axial_force_f))

        # if self.load_moment > self.section.moment_capacity:
        #     self.member_capacity = False
        #     logger.warning(' : Moment load is exceeding moment capacity  %2.2f KN-m' % self.section.moment_capacity)
        #     logger.error(" : Design is not safe. \n ")
        #     logger.debug(" :=========End Of design===========")
        # else:
        #     self.member_capacity = True
        #     self.moment_web = (Z_w * self.load_moment / (
        #         self.section.plast_sec_mod_z))  # Nm todo add in ddcl # z_w of web & z_p  of section
        #     self.moment_flange = ((self.load_moment) - self.moment_web)
        #     self.sectioncheck(self)

        if len(self.flange_plate.thickness) >= 2:
            self.max_thick_f = max(self.flange_plate.thickness)
        else:
            self.max_thick_f = self.flange_plate.thickness[0]
        if len(self.web_plate.thickness) >= 2:
            self.max_thick_w = max(self.web_plate.thickness)
        else:
            self.max_thick_w = self.web_plate.thickness[0]
        ###########################################################
        if self.factored_axial_load > self.axial_capacity:
            logger.warning(' : Factored axial load is exceeding axial capacity  %2.2f KN' % self.axial_capacity)
            logger.error(" : Design is not safe. \n ")
            logger.debug(" :=========End Of design===========")
            self.member_capacity_status = False
        else:
            if self.fact_shear_load > self.shear_capacity1:
                logger.warning(' : Factored shear load is exceeding shear capacity  %2.2f KN' % self.shear_capacity1)
                logger.error(" : Design is not safe. \n ")
                logger.debug(" :=========End Of design===========")
                self.member_capacity_status = False
            else:
                if self.load_moment > self.section.moment_capacity:
                    self.member_capacity_status = False
                    logger.warning(
                        ' : Moment load is exceeding moment capacity  %2.2f KN-m' % self.section.moment_capacity)
                    logger.error(" : Design is not safe. \n ")
                    logger.debug(" :=========End Of design===========")
                else:
                    self.member_capacity_status = True

                    # self.moment_web = (Z_w * self.load_moment / (
                    #     self.section.plast_sec_mod_z))  # Nm todo add in ddcl # z_w of web & z_p  of section
                    # self.moment_flange = ((self.load_moment) - self.moment_web)
                    self.initial_pt_thk(self)

        # #############################################################
        # else :
        #     self.member_capacity = False
        #     logger.error(" : Load applied is greater than member capacity. \n ")
        #     logger.error(" : Design is not safe. \n ")
        #     logger.debug(" :=========End Of design===========")

    def initial_pt_thk(self):
        ############################### WEB MENBER CAPACITY CHECK ############################
        ###### # capacity Check for web in axial = min(block, yielding, rupture)
        self.initial_pt_thk_status = False
        # self.axial_force_w = ((self.section.depth - (2 * self.section.flange_thickness)) * self.section.web_thickness * self.factored_axial_load) / (
        #                          self.section.area)  # N
        A_v_web = (self.section.depth - 2 * self.section.flange_thickness) * self.section.web_thickness

        self.section.tension_yielding_capacity_web = self.tension_member_design_due_to_yielding_of_gross_section(
            A_v=A_v_web,
            fy=self.section.fy)

        if self.section.tension_yielding_capacity_web > self.axial_force_w:

            ################################# FLANGE MEMBER CAPACITY CHECK##############################
            # self.axial_force_f = self.factored_axial_load * self.section.flange_width * self.section.flange_thickness / (self.section.area)  # N
            # self.flange_force = (((self.moment_flange) / (self.section.depth - self.section.flange_thickness)) + (self.axial_force_f))

            A_v_flange = self.section.flange_thickness * self.section.flange_width
            self.section.tension_yielding_capacity = self.tension_member_design_due_to_yielding_of_gross_section(
                A_v=A_v_flange,
                fy=self.flange_plate.fy)
            if self.section.tension_yielding_capacity > self.flange_force:
                # if len(self.web_plate.thickness) >= 2:
                #     self.max_thick_w = max(self.web_plate.thickness)
                # else:
                #     self.max_thick_w = self.web_plate.thickness[0]

                self.web_plate_thickness_possible = [i for i in self.web_plate.thickness if
                                                     i >= (self.section.web_thickness / 2)]

                # if len(self.flange_plate.thickness) >= 2:
                #     self.max_thick_f = max(self.flange_plate.thickness)
                # else:
                #     self.max_thick_f = self.flange_plate.thickness[0]

                if self.preference == "Outside":
                    self.flange_plate_thickness_possible = [i for i in self.flange_plate.thickness if
                                                            i >= self.section.flange_thickness]
                else:
                    self.flange_plate_thickness_possible = [i for i in self.flange_plate.thickness if
                                                            i >= (self.section.flange_thickness / 2)]

                if len(self.flange_plate_thickness_possible) == 0 or len(self.web_plate_thickness_possible) == 0:
                    logger.error(" : Flange and web Plate thickness should be greater than section  thicknesss.")
                    self.initial_pt_thk_status = False
                else:
                    self.flange_plate.thickness_provided = self.min_thick_based_on_area(self,
                                                                                        tk=self.section.flange_thickness,
                                                                                        width=self.section.flange_width,
                                                                                        list_of_pt_tk=self.flange_plate_thickness_possible,
                                                                                        t_w=self.section.web_thickness,
                                                                                        r_1=self.section.root_radius,
                                                                                        D=self.section.depth,
                                                                                        preference=self.preference)
                    self.web_plate.thickness_provided = self.min_thick_based_on_area(self,
                                                                                     tk=self.section.flange_thickness,
                                                                                     width=self.section.flange_width,
                                                                                     list_of_pt_tk=self.web_plate_thickness_possible,
                                                                                     t_w=self.section.web_thickness,
                                                                                     r_1=self.section.root_radius,
                                                                                     D=self.section.depth, )
                    # self.flange_plate_crs_sec_area= round(self.flange_plate_crs_sec_area)
                    # self.web_crs_area = round(self.web_crs_area)
                    # self.web_plate_crs_sec_area = round(self.web_plate_crs_sec_area)
                    if self.web_plate.thickness_provided == 0 or self.flange_plate.thickness_provided == 0:
                        self.initial_pt_thk_status = False
                        logger.warning(" : Plate is not possible")
                        logger.error(" : Design is not safe. \n ")
                        logger.debug(" : =========End Of design===========")
                    else:
                        self.initial_pt_thk_status = True
                        self.select_bolt_dia(self)
            else:
                self.initial_pt_thk_status = False
                logger.warning(
                    " : Tension_yielding_capacity  of flange is less than applied loads, Please select larger sections or decrease loads")
                logger.error(" : Design is not safe. \n ")
                logger.debug(" : =========End Of design===========")

        else:
            self.initial_pt_thk_status = False
            logger.warning(
                " : Tension_yielding_capacity of web  is less than applied loads, Please select larger sections or decrease loads")
            logger.error(" : Design is not safe. \n ")
            logger.debug(" : =========End Of design===========")

    def select_bolt_dia(self):
        self.min_plate_height = self.section.flange_width
        self.max_plate_height = self.section.flange_width

        axial_force_f =  self.factored_axial_load  * self.section.flange_width * \
                         self.section.flange_thickness / (self.section.area )

        self.flange_force = ((( self.moment_flange) / (self.section.depth - self.section.flange_thickness)) +(axial_force_f))
        self.res_force = math.sqrt((self.fact_shear_load)** 2 + ( self.factored_axial_load ) ** 2) #N

        bolts_required_previous_1 = 2
        bolts_required_previous_2 = 2
        bolt_diameter_previous = self.bolt.bolt_diameter[-1]

        self.bolt.bolt_grade_provided = self.bolt.bolt_grade[-1]
        count_1 = 0
        count_2 = 0
        bolts_one_line = 1
        ###### for flange plate thickness####
        self.bolt_conn_plates_t_fu_fy = []
        if self.preference == "Outside":
            self.bolt_conn_plates_t_fu_fy.append((self.flange_plate.thickness_provided, self.flange_plate.fu, self.flange_plate.fy))
            self.bolt_conn_plates_t_fu_fy.append(
                (self.section.flange_thickness, self.section.fu, self.section.fy))
        else:
            self.bolt_conn_plates_t_fu_fy.append(
                (2*self.flange_plate.thickness_provided, self.flange_plate.fu, self.flange_plate.fy))
            self.bolt_conn_plates_t_fu_fy.append(
                (self.section.flange_thickness, self.section.fu, self.section.fy))

        ##### for web plate thickness######
        self.bolt_conn_plates_web_t_fu_fy = []
        self.bolt_conn_plates_web_t_fu_fy.append(
            ( 2*self.web_plate.thickness_provided, self.web_plate.fu, self.web_plate.fy))
        self.bolt_conn_plates_web_t_fu_fy.append(
            (self.section.web_thickness, self.section.fu, self.section.fy))
        bolt_design_status_1 = False
        bolt_design_status_2= False
        for self.bolt.bolt_diameter_provided in reversed(self.bolt.bolt_diameter):

            self.flange_bolt.calculate_bolt_spacing_limits(bolt_diameter_provided=self.bolt.bolt_diameter_provided,
                                                        conn_plates_t_fu_fy=self.bolt_conn_plates_t_fu_fy)
            print(self.flange_bolt.min_edge_dist, self.flange_bolt.edge_type)

            if self.preference == "Outside":
                self.flange_bolt.calculate_bolt_capacity(bolt_diameter_provided=self.bolt.bolt_diameter_provided,
                                                         bolt_grade_provided=self.bolt.bolt_grade_provided,
                                                         conn_plates_t_fu_fy=self.bolt_conn_plates_t_fu_fy,
                                                         n_planes=1)
            else:
                self.flange_bolt.calculate_bolt_capacity(bolt_diameter_provided=self.bolt.bolt_diameter_provided,
                                                         bolt_grade_provided=self.bolt.bolt_grade_provided,
                                                         conn_plates_t_fu_fy=self.bolt_conn_plates_t_fu_fy,
                                                         n_planes=2)

            self.web_bolt.calculate_bolt_spacing_limits(bolt_diameter_provided=self.bolt.bolt_diameter_provided,
                                                        conn_plates_t_fu_fy= self.bolt_conn_plates_web_t_fu_fy)

            self.web_bolt.calculate_bolt_capacity(bolt_diameter_provided=self.bolt.bolt_diameter_provided,
                                                     bolt_grade_provided=self.bolt.bolt_grade_provided,
                                                     conn_plates_t_fu_fy= self.bolt_conn_plates_web_t_fu_fy,
                                                     n_planes=2)

            self.flange_plate.get_flange_plate_details(bolt_dia=self.flange_bolt.bolt_diameter_provided,
                                                    flange_plate_h_min=self.min_plate_height,
                                                    flange_plate_h_max=self.max_plate_height,
                                                    bolt_capacity=self.flange_bolt.bolt_capacity,
                                                    min_edge_dist=self.flange_bolt.min_edge_dist_round,
                                                    min_gauge=self.flange_bolt.min_gauge_round,
                                                    max_spacing=self.flange_bolt.max_spacing_round,
                                                    max_edge_dist=self.flange_bolt.max_edge_dist_round,
                                                    axial_load=self.flange_force, gap=self.flange_plate.gap/2,
                                                    web_thickness =self.section.web_thickness,
                                                    root_radius= self.section.root_radius)



            self.min_web_plate_height = self.section.min_plate_height()
            self.max_web_plate_height = self.section.max_plate_height()
            self.axial_force_w = ((self.section.depth - (2 * self.section.flange_thickness)) *
                                  self.section.web_thickness *
                                  self.factored_axial_load) / (self.section.area )

            self.web_plate.get_web_plate_details(bolt_dia=self.bolt.bolt_diameter_provided,
                                                 web_plate_h_min=self.min_web_plate_height,
                                                 web_plate_h_max=self.max_web_plate_height,
                                                 bolt_capacity=self.web_bolt.bolt_capacity,
                                                 min_edge_dist=self.web_bolt.min_edge_dist_round,
                                                 min_gauge=self.web_bolt.min_gauge_round,
                                                 max_spacing=self.web_bolt.max_spacing_round,
                                                 max_edge_dist=self.web_bolt.max_edge_dist_round
                                                 ,shear_load=self.fact_shear_load ,
                                                 axial_load=self.axial_force_w,
                                                 web_moment = self.moment_web,
                                                 gap=(self.web_plate.gap/2), shear_ecc=True,joint = "half")



            if self.flange_plate.design_status is True and self.web_plate.design_status is True:
                if self.flange_plate.bolts_required > bolts_required_previous_1 and count_1 >= 1:
                    self.bolt.bolt_diameter_provided = bolt_diameter_previous
                    self.flange_plate.bolts_required = bolts_required_previous_1
                    self.flange_plate.bolt_force = bolt_force_previous_1
                    bolt_design_status_1 = self.flange_plate.design_status
                    break
                bolts_required_previous_1 = self.flange_plate.bolts_required
                bolt_diameter_previous = self.bolt.bolt_diameter_provided
                bolt_force_previous_1 = self.flange_plate.bolt_force
                count_1 += 1
                bolt_design_status_1 = self.flange_plate.design_status

                if self.web_plate.bolts_required > bolts_required_previous_2 and count_2 >= 1:
                    self.bolt.bolt_diameter_provided = bolt_diameter_previous
                    self.web_plate.bolts_required = bolts_required_previous_2
                    self.web_plate.bolt_force = bolt_force_previous_2
                    bolt_design_status_2 = self.web_plate.design_status
                    break
                bolts_required_previous_2 = self.web_plate.bolts_required
                bolt_diameter_previous = self.bolt.bolt_diameter_provided
                bolt_force_previous_2 = self.web_plate.bolt_force
                count_2 += 1
                bolt_design_status_2 = self.web_plate.design_status

        bolt_capacity_req = self.bolt.bolt_capacity

        if (self.flange_plate.design_status == False and bolt_design_status_1 != True ) or (self.web_plate.design_status == False and bolt_design_status_2 != True ):
            self.design_status = False
        else:
            self.bolt.bolt_diameter_provided = bolt_diameter_previous
            self.flange_plate.bolts_required = bolts_required_previous_1
            self.flange_plate.bolt_force = bolt_force_previous_1
            self.web_plate.bolts_required = bolts_required_previous_2
            self.web_plate.bolt_force = bolt_force_previous_2

        if bolt_design_status_1 is True and bolt_design_status_2 is True  :
            self.design_status = True
            self.get_bolt_grade(self)
        else:
            self.design_status = False
            logger.error("Bolt Not Possible")
            logger.error(" : Design is not safe. \n ")
            logger.debug(" : =========End Of design===========")

    def get_bolt_grade(self):
        print(self.design_status, "Getting bolt grade")
        bolt_grade_previous = self.bolt.bolt_grade[-1]
        grade_status = False
        for self.bolt.bolt_grade_provided in reversed(self.bolt.bolt_grade):
            count = 1
            self.flange_bolt.calculate_bolt_spacing_limits(bolt_diameter_provided=self.bolt.bolt_diameter_provided,
                                                           conn_plates_t_fu_fy=self.bolt_conn_plates_t_fu_fy)

            if self.preference == "Outside":
                self.flange_bolt.calculate_bolt_capacity(bolt_diameter_provided=self.bolt.bolt_diameter_provided,
                                                         bolt_grade_provided=self.bolt.bolt_grade_provided,
                                                         conn_plates_t_fu_fy=self.bolt_conn_plates_t_fu_fy,
                                                         n_planes=1)
            else:
                self.flange_bolt.calculate_bolt_capacity(bolt_diameter_provided=self.bolt.bolt_diameter_provided,
                                                         bolt_grade_provided=self.bolt.bolt_grade_provided,
                                                         conn_plates_t_fu_fy=self.bolt_conn_plates_t_fu_fy,
                                                         n_planes=2)

            self.web_bolt.calculate_bolt_spacing_limits(bolt_diameter_provided=self.bolt.bolt_diameter_provided,
                                                        conn_plates_t_fu_fy=self.bolt_conn_plates_web_t_fu_fy)

            self.web_bolt.calculate_bolt_capacity(bolt_diameter_provided=self.bolt.bolt_diameter_provided,
                                                  bolt_grade_provided=self.bolt.bolt_grade_provided,
                                                  conn_plates_t_fu_fy=self.bolt_conn_plates_web_t_fu_fy,
                                                  n_planes=2)

            print(self.bolt.bolt_grade_provided, self.bolt.bolt_capacity, self.flange_plate.bolt_force)

            bolt_capacity_reduced_flange = self.flange_plate.get_bolt_red(self.flange_plate.bolts_one_line,
                                                                          self.flange_plate.gauge_provided,self.web_plate.bolt_line,self.web_plate.pitch_provided,
                                                                          self.flange_bolt.bolt_capacity,
                                                                          self.bolt.bolt_diameter_provided,)
            bolt_capacity_reduced_web = self.web_plate.get_bolt_red(self.web_plate.bolts_one_line,
                                                                    self.web_plate.gauge_provided,self.web_plate.bolt_line,self.web_plate.pitch_provided,
                                                                    self.web_bolt.bolt_capacity,
                                                                    self.bolt.bolt_diameter_provided)
            if ( bolt_capacity_reduced_flange < self.flange_plate.bolt_force) and  (bolt_capacity_reduced_web  < self.web_plate.bolt_force) and (count >= 1):
                self.bolt.bolt_grade_provided = bolt_grade_previous
                grade_status = True
                break
            bolt_grade_previous = self.bolt.bolt_grade_provided
            grade_status = True
            count += 1

        if grade_status == False:
            self.design_status = False

        else:
            self.bolt.bolt_grade_provided = bolt_grade_previous
            self.get_plate_details(self)


    def get_plate_details(self):

        self.min_plate_height = self.section.flange_width
        self.max_plate_height = self.section.flange_width

        axial_force_f = self.factored_axial_load * self.section.flange_width * \
                        self.section.flange_thickness / (self.section.area)

        self.flange_force = (((self.moment_flange) / (self.section.depth - self.section.flange_thickness)) +
                             (axial_force_f))
        self.flange_bolt.calculate_bolt_spacing_limits(bolt_diameter_provided=self.bolt.bolt_diameter_provided,
                                                       conn_plates_t_fu_fy=self.bolt_conn_plates_t_fu_fy)

        if self.preference == "Outside":
            self.flange_bolt.calculate_bolt_capacity(bolt_diameter_provided=self.bolt.bolt_diameter_provided,
                                                     bolt_grade_provided=self.bolt.bolt_grade_provided,
                                                     conn_plates_t_fu_fy=self.bolt_conn_plates_t_fu_fy,
                                                     n_planes=1)
        else:
            self.flange_bolt.calculate_bolt_capacity(bolt_diameter_provided=self.bolt.bolt_diameter_provided,
                                                     bolt_grade_provided=self.bolt.bolt_grade_provided,
                                                     conn_plates_t_fu_fy=self.bolt_conn_plates_t_fu_fy,
                                                     n_planes=2)

        self.web_bolt.calculate_bolt_spacing_limits(bolt_diameter_provided=self.bolt.bolt_diameter_provided,
                                                    conn_plates_t_fu_fy=self.bolt_conn_plates_web_t_fu_fy)

        self.web_bolt.calculate_bolt_capacity(bolt_diameter_provided=self.bolt.bolt_diameter_provided,
                                              bolt_grade_provided=self.bolt.bolt_grade_provided,
                                              conn_plates_t_fu_fy=self.bolt_conn_plates_web_t_fu_fy,
                                              n_planes=2)

        self.flange_plate.get_flange_plate_details(bolt_dia=self.flange_bolt.bolt_diameter_provided,
                                                   flange_plate_h_min=self.min_plate_height,
                                                   flange_plate_h_max=self.max_plate_height,
                                                   bolt_capacity=self.flange_bolt.bolt_capacity,
                                                   min_edge_dist=self.flange_bolt.min_edge_dist_round,
                                                   min_gauge=self.flange_bolt.min_gauge_round,
                                                   max_spacing=self.flange_bolt.max_spacing_round,
                                                   max_edge_dist=self.flange_bolt.max_edge_dist_round,
                                                   axial_load=self.flange_force,gap=self.flange_plate.gap/2,
                                                   web_thickness=self.section.web_thickness,
                                                   root_radius=self.section.root_radius,joint = "half")

        self.min_web_plate_height = self.section.min_plate_height()
        self.max_web_plate_height = self.section.max_plate_height()
        axial_force_w = ((self.section.depth - (2 * self.section.flange_thickness)) *
                         self.section.web_thickness * self.factored_axial_load) / (
                         self.section.area)

        self.web_plate.get_web_plate_details(bolt_dia=self.web_bolt.bolt_diameter_provided,
                                             web_plate_h_min=self.min_web_plate_height,
                                             web_plate_h_max=self.max_web_plate_height,
                                             bolt_capacity=self.web_bolt.bolt_capacity,
                                             min_edge_dist=self.web_bolt.min_edge_dist_round,
                                             min_gauge=self.web_bolt.min_gauge_round,
                                             max_spacing=self.web_bolt.max_spacing_round,
                                             max_edge_dist=self.web_bolt.max_edge_dist_round
                                             , shear_load=self.fact_shear_load, axial_load=self.axial_force_w,web_moment = self.moment_web,

                                             gap=(self.web_plate.gap/2), shear_ecc=True,joint = "half")

        possible_inner_plate = self.section.flange_width / 2 - self.section.web_thickness / 2 - self.section.root_radius
        self.flange_plate.edge_dist_provided = (possible_inner_plate- (self.flange_plate.gauge_provided *
                                                                       (self.flange_plate.bolts_one_line-1)))/2


        if self.flange_plate.design_status is False or self.flange_plate.design_status is False :
            self.design_status = False
            logger.error("bolted connection not possible")
            logger.error(" : Design is not safe. \n ")
            logger.debug(" : =========End Of design===========")

        else:
           self.member_check(self)

        ################################################################
        ##################################################################
    def member_check(self):
        ###### # capacity Check for flange = min(block, yielding, rupture)
        #### Block shear capacity of  flange ### #todo comment out

        axial_force_f = self.factored_axial_load * self.section.flange_width * self.section.flange_thickness / (
                        self.section.area)
        self.flange_force = (((self.moment_flange) / (self.section.depth - self.section.flange_thickness)) + (
                            axial_force_f))

        A_vn_flange = (self.section.flange_width - self.flange_plate.bolts_one_line * self.flange_bolt.dia_hole) * \
                      self.section.flange_thickness
        A_v_flange = self.section.flange_thickness * self.flange_plate.height

        self.section.tension_yielding_capacity= self.tension_member_design_due_to_yielding_of_gross_section(
                                                A_v=A_v_flange,
                                                fy=self.flange_plate.fy)

        self.section.tension_rupture_capacity = self.tension_member_design_due_to_rupture_of_critical_section(
                                                A_vn=A_vn_flange,
                                                fu=self.flange_plate.fu)
        #  Block shear strength for flange
        design_status_block_shear = False
        edge_dist = self.flange_plate.edge_dist_provided
        end_dist = self.flange_plate.end_dist_provided
        gauge = self.flange_plate.gauge_provided
        pitch = self.flange_plate.pitch_provided

        while design_status_block_shear == False:

            Avg = 2 * (end_dist + (self.flange_plate.bolt_line - 1) * self.flange_plate.pitch_provided) \
                       * self.section.flange_thickness
            Avn = 2 * (self.flange_plate.end_dist_provided + (self.flange_plate.bolt_line - 1) *
                       self.flange_plate.pitch_provided - (self.flange_plate.bolt_line - 0.5) *
                       self.flange_bolt.dia_hole) * self.section.flange_thickness
            Atg = 2 * (( self.flange_plate.bolts_one_line / 2 - 1) * self.flange_plate.gauge_provided +
                       self.flange_plate.edge_dist_provided) * self.section.flange_thickness

            Atn = 2 * ((self.flange_plate.bolts_one_line / 2 - 1) * self.flange_plate.gauge_provided -
                       ((self.flange_plate.bolts_one_line / 2 - 0.5) * self.flange_bolt.dia_hole) +
                       self.flange_plate.edge_dist_provided) * \
                       self.section.flange_thickness

            self.section.block_shear_capacity = self.block_shear_strength_section(A_vg=Avg, A_vn=Avn, A_tg=Atg,
                                                                                  A_tn=Atn,
                                                                                  f_u=self.flange_plate.fu,
                                                                                  f_y=self.flange_plate.fy)

            if self.section.block_shear_capacity <  self.flange_force:
                if self.flange_bolt.max_spacing_round >= pitch + 5 and self.flange_bolt.max_end_dist_round >= end_dist + 5:  # increase thickness todo
                    if self.flange_plate.bolt_line == 1:
                        end_dist += 5
                    else:
                        pitch += 5
                else:
                    break
            else:
                design_status_block_shear = True
                break

            if design_status_block_shear is True:
                break
        if design_status_block_shear is True:
            self.section.tension_capacity_flange = min(self.section.tension_yielding_capacity, self.section.tension_rupture_capacity,
                                                       self.section.block_shear_capacity)
            if self.section.tension_capacity_flange  < self.flange_force:
                self.design_status = False
                logger.warning(": Tension capacity of flange is less than required flange force %2.2f KN" % self.flange_force)
                logger.info(": Select larger beam section or decrease the applied loads")
                logger.error(" : Design is not safe. \n ")
                logger.debug(" : =========End Of design===========")
            else:
                self.design_status = True
                self.flange_plate_check(self)
        else:
            self.design_status = False
            logger.warning(": Block Shear of flange is less than required flange force %2.2f KN" % self.flange_force)
            logger.info(": Select the larger section")
            logger.error(" : Design is not safe. \n ")
            logger.debug(" : =========End Of design===========")

    def flange_plate_check(self):
        # capacity Check for flange_outside_plate =min(block, yielding, rupture)
        ####Capacity of flange cover plate for bolted Outside #
        self.axial_force_f = self.factored_axial_load * self.section.flange_width * self.section.flange_thickness / (self.section.area)
        self.flange_force = (((self.moment_flange) / (self.section.depth - self.section.flange_thickness)) + self.axial_force_f)

        if self.preference == "Outside":
            #  Block shear strength for outside flange plate
            # available_flange_thickness = list([x for x in self.flange_plate.thickness if (self.flange_plate.thickness_provided <= x)])
            #
            # for self.flange_plate.thickness_provided in available_flange_thickness:
            design_status_block_shear = False
            edge_dist = self.flange_plate.edge_dist_provided
            end_dist = self.flange_plate.end_dist_provided
            gauge = self.flange_plate.gauge_provided
            pitch = self.flange_plate.pitch_provided

            A_vn_flange = (self.section.flange_width - self.flange_plate.bolts_one_line * self.flange_bolt.dia_hole) * \
                          self.flange_plate.thickness_provided
            A_v_flange = self.flange_plate.thickness_provided * self.flange_plate.height
            self.flange_plate.tension_yielding_capacity = self.tension_member_design_due_to_yielding_of_gross_section(
                                                            A_v=A_v_flange,
                                                            fy=self.flange_plate.fy)

            self.flange_plate.tension_rupture_capacity = self.tension_member_design_due_to_rupture_of_critical_section(
                                                            A_vn=A_vn_flange,
                                                            fu=self.flange_plate.fu)

            #### Block shear capacity of flange plate ###
            while design_status_block_shear == False:

                Avg = 2 * (self.flange_plate.end_dist_provided + (self.flange_plate.bolt_line - 1) * self.flange_plate.pitch_provided) * self.flange_plate.thickness_provided
                Avn = 2 * (self.flange_plate.end_dist_provided + (self.flange_plate.bolt_line - 1)
                           * self.flange_plate.pitch_provided - (self.flange_plate.bolt_line - 0.5) *
                           self.flange_bolt.dia_hole) *  self.flange_plate.thickness_provided
                Atg = 2 * ((((self.flange_plate.bolts_one_line / 2 - 1) * self.flange_plate.gauge_provided) + (
                            self.flange_plate.edge_dist_provided + self.section.root_radius + self.section.web_thickness / 2))
                           * self.flange_plate.thickness_provided)
                Atn = 2 * (((((self.flange_plate.bolts_one_line / 2 - 1) * self.flange_plate.gauge_provided) - (
                         self.flange_plate.bolts_one_line / 2 - 0.5) * self.flange_bolt.dia_hole)) + (
                         self.flange_plate.edge_dist_provided + self.section.root_radius + self.section.web_thickness / 2)) \
                         * self.flange_plate.thickness_provided
#

                self.flange_plate.block_shear_capacity = self.block_shear_strength_plate(A_vg=Avg, A_vn=Avn,
                                                                                         A_tg=Atg,
                                                                                         A_tn=Atn,
                                                                                         f_u=self.flange_plate.fu,
                                                                                         f_y=self.flange_plate.fy)
                if self.flange_plate.block_shear_capacity < self.flange_force :
                    if self.flange_bolt.max_spacing_round >= pitch + 5 and self.flange_bolt.max_end_dist_round >= end_dist + 5:  # increase thickness todo
                        if self.flange_plate.bolt_line == 1:
                            end_dist += 5
                        else:
                            pitch += 5
                    else:
                        break
                else:
                    design_status_block_shear = True
                    break
            # if design_status_block_shear is True:
            #     break

            if design_status_block_shear is True:
                self.flange_plate.tension_capacity_flange_plate= min(self.flange_plate.tension_yielding_capacity,
                                                    self.flange_plate.tension_rupture_capacity,
                                                    self.flange_plate.block_shear_capacity)

                if self.flange_plate.tension_capacity_flange_plate < self.flange_force:
                    self.design_status = False
                    logger.warning(": Tension capacity of flange plate  is less than required flange force %2.2f KN" % self.flange_force)
                    logger.info(": Select larger beam section or decrease the applied loads")
                    logger.error(" : Design is not safe. \n ")
                    logger.debug(" : =========End Of design===========")
                else:
                    self.design_status = True
                    self.web_axial_check(self)
            else:
                self.design_status = False
                logger.warning(": Block Shear of flange plate is less than required flange force %2.2f KN" % self.flange_force)
                logger.info(": Increase the plate thickness")
                logger.error(" : Design is not safe. \n ")
                logger.debug(" : =========End Of design===========")

        else:
            # capacity Check for flange_outsite_plate =min(block, yielding, rupture)
            #  Block shear strength for outside + inside flange plate
            # OUTSIDE-inside
            # available_flange_thickness = list(
            #     [x for x in self.flange_plate.thickness if ((self.flange_plate.thickness_provided) <= x)])
            #
            # for self.flange_plate.thickness_provided in available_flange_thickness:
            design_status_block_shear = False
            edge_dist = self.flange_plate.edge_dist_provided
            end_dist = self.flange_plate.end_dist_provided
            gauge = self.flange_plate.gauge_provided
            pitch = self.flange_plate.pitch_provided

            #  yielding,rupture  for  inside flange plate
            self.flange_plate.Innerheight = (self.section.flange_width - self.section.web_thickness - (self.section.root_radius * 2)) / 2
            flange_plate_height_outside = self.flange_plate.height
            self.flange_plate.Innerlength = self.flange_plate.length

            A_vn_flange = (((2 * self.flange_plate.Innerheight ) + self.section.flange_width) - (self.flange_plate.bolts_one_line * self.flange_bolt.dia_hole)) * self.flange_plate.thickness_provided
            A_v_flange = ((2 *self.flange_plate.Innerheight ) + self.section.flange_width) * self.flange_plate.thickness_provided
            self.flange_plate.tension_yielding_capacity = self.tension_member_design_due_to_yielding_of_gross_section(
                A_v=A_v_flange,
                fy=self.flange_plate.fy)


            self.flange_plate.tension_rupture_capacity = self.tension_member_design_due_to_rupture_of_critical_section(
                A_vn=A_vn_flange,
                fu=self.flange_plate.fu)
            #### Block shear capacity of flange plate ###

            while design_status_block_shear == False:

                Avg = 2 * (self.flange_plate.end_dist_provided + (
                        self.flange_plate.bolt_line - 1) * self.flange_plate.pitch_provided) * self.flange_plate.thickness_provided
                Avn = 2 * (self.flange_plate.end_dist_provided + (
                        self.flange_plate.bolt_line - 1) * self.flange_plate.pitch_provided - (
                                   self.flange_plate.bolt_line - 0.5) * self.flange_bolt.dia_hole) * \
                      self.flange_plate.thickness_provided
                Atg = 2*((((self.flange_plate.bolts_one_line/2 - 1) * self.flange_plate.gauge_provided) + (self.flange_plate.edge_dist_provided +self.section.root_radius + self.section.web_thickness/2))
                     * self.flange_plate.thickness_provided) #
                Atn =  2*(((((self.flange_plate.bolts_one_line/2 - 1) * self.flange_plate.gauge_provided) - (
                        self.flange_plate.bolts_one_line/2 - 0.5) * self.flange_bolt.dia_hole)) +
                          (self.flange_plate.edge_dist_provided +self.section.root_radius + self.section.web_thickness/2)) * self.flange_plate.thickness_provided

                self.flange_plate_block_shear_capactity_outside = self.block_shear_strength_plate(A_vg=Avg, A_vn=Avn,
                                                                                             A_tg=Atg,
                                                                                             A_tn=Atn,
                                                                                             f_u=self.flange_plate.fu,
                                                                                             f_y=self.flange_plate.fy)

                #  Block shear strength for inside flange plate under AXIAL
                Avg = 2 * (self.flange_plate.end_dist_provided + (
                        self.flange_plate.bolt_line - 1) * self.flange_plate.pitch_provided) \
                      * self.flange_plate.thickness_provided
                Avn = 2 * (self.flange_plate.end_dist_provided + (
                        self.flange_plate.bolt_line - 1) * self.flange_plate.pitch_provided - (
                                   self.flange_plate.bolt_line - 0.5) * self.flange_bolt.dia_hole) * \
                      self.flange_plate.thickness_provided

                Atg = 2 * ((self.flange_plate.bolts_one_line/2  - 1) * self.flange_plate.gauge_provided + self.flange_plate.edge_dist_provided )* \
                      self.flange_plate.thickness_provided
                # todo add in DDCl and diagram
                Atn = 2 * ((self.flange_plate.bolts_one_line/2  - 1) *
                           self.flange_plate.gauge_provided - ((self.flange_plate.bolts_one_line/2  - 0.5) * self.flange_bolt.dia_hole)+ self.flange_plate.edge_dist_provided )* \
                      self.flange_plate.thickness_provided
                # todo add in DDCl
                self.flange_plate_block_shear_capacity_inside = self.block_shear_strength_plate(A_vg=Avg, A_vn=Avn,
                                                                                           A_tg=Atg,
                                                                                           A_tn=Atn,
                                                                                           f_u=self.flange_plate.fu,
                                                                                           f_y=self.flange_plate.fy)
                self.flange_plate.block_shear_capacity = self.flange_plate_block_shear_capactity_outside + self.flange_plate_block_shear_capacity_inside

                if self.flange_plate.block_shear_capacity <  self.flange_force :
                    if self.flange_bolt.max_spacing_round >= pitch + 5 and self.flange_bolt.max_end_dist_round >= end_dist + 5:  # increase thickness todo
                        if self.flange_plate.bolt_line == 1:
                            end_dist += 5
                        else:
                            pitch += 5
                    else:
                        break
                else:
                    design_status_block_shear = True
                    break
            # if design_status_block_shear is True:
            #     break

            if design_status_block_shear is True:
                self.flange_plate.tension_capacity_flange_plate = min(self.flange_plate.tension_yielding_capacity,
                                                    self.flange_plate.tension_rupture_capacity,
                                                    self.flange_plate.block_shear_capacity)
                print ("flange_force",self.flange_force)
                print(self.flange_plate.tension_capacity_flange_plate, "tension_capacity_flange_plate")
                if  self.flange_plate.tension_capacity_flange_plate < self.flange_force:
                    self.design_status = False
                    logger.warning(": Tension capacity of flange plate  is less than required flange force %2.2f KN" % self.flange_force)
                    logger.info(": Select larger beam section or decrease the applied loads")
                    logger.error(" : Design is not safe. \n ")
                    logger.debug(" : =========End Of design===========")
                else:
                    self.design_status = True
                    self.web_axial_check(self)
            else:
                self.design_status = False
                logger.warning(": Block Shear of flange plate is less than required flange force %2.2f KN" % self.flange_force)
                logger.info(": Increase the plate thickness")
                logger.error(" : Design is not safe. \n ")
                logger.debug(" : =========End Of design===========")

        ######################################################################### ##
                    # Design of web splice plate

    ################################ CAPACITY CHECK FOR WEB #####################################################################################

    def web_axial_check(self):
        self.axial_force_w = ((self.section.depth - (2 * self.section.flange_thickness)) * self.section.web_thickness *  self.factored_axial_load ) / (self.section.area )

        ###### # capacity Check for web in axial = min(block, yielding, rupture)
        A_vn_web =  (( self.section.depth - (2 * self.section.flange_thickness) - (self.web_plate.bolts_one_line * self.web_bolt.dia_hole))) \
                   * self.section.web_thickness
        A_v_web = (self.section.depth - 2 * self.section.flange_thickness) * self.section.web_thickness
        self.section.tension_yielding_capacity_web = self.tension_member_design_due_to_yielding_of_gross_section(
            A_v=A_v_web, fy=self.web_plate.fy)
        self.section.tension_rupture_capacity_web = self.tension_member_design_due_to_rupture_of_critical_section(
            A_vn=A_vn_web, fu=self.web_plate.fu)

        design_status_block_shear = False
        edge_dist = self.web_plate.edge_dist_provided
        end_dist = self.web_plate.end_dist_provided
        gauge = self.web_plate.gauge_provided
        pitch = self.web_plate.pitch_provided

        #### Block shear capacity of web in axial ###
        while design_status_block_shear == False:
            Avg = 2 * ((self.web_plate.bolt_line - 1) * pitch + end_dist) * \
                  self.section.web_thickness
            Avn = 2 * ((self.web_plate.bolt_line - 1) * pitch + (
                    self.web_plate.bolt_line - 0.5) * self.web_bolt.dia_hole + end_dist) * \
                  self.section.web_thickness
            Atg = (self.web_plate.edge_dist_provided + (
                    self.web_plate.bolts_one_line - 1) * gauge) * self.section.web_thickness
            Atn = (self.web_plate.edge_dist_provided + (
                    self.web_plate.bolts_one_line - 1) * gauge - (
                           self.web_plate.bolts_one_line - 1) * self.web_bolt.dia_hole) * self.section.web_thickness

            self.section.block_shear_capacity_web = self.block_shear_strength_section(A_vg=Avg, A_vn=Avn, A_tg=Atg,
                                                                                    A_tn=Atn,
                                                                                    f_u=self.web_plate.fu,
                                                                                    f_y=self.web_plate.fy)

            if self.section.block_shear_capacity_web <  self.axial_force_w :
                if self.web_bolt.max_spacing_round >= pitch + 5 and self.web_bolt.max_end_dist_round >= end_dist + 5:  # increase thickness todo
                    if self.web_plate.bolt_line == 1:
                        end_dist += 5
                    else:
                        pitch += 5
                else:
                    break
            else:
                design_status_block_shear = True
                break
        if design_status_block_shear == True:
            self.section.tension_capacity_web = min(self.section.tension_yielding_capacity_web, self.section.tension_rupture_capacity_web,
                                             self.section.block_shear_capacity_web)

            self.axial_force_w = ((self.section.depth - (2 * self.section.flange_thickness)) * self.section.web_thickness *  self.factored_axial_load ) / (self.section.area )
            if self.section.tension_capacity_web < self.axial_force_w:
                self.design_status = False
                logger.warning(": Tension capacity of web is less than required axial_force_w %2.2f KN" % self.axial_force_w)
                logger.info(": Select larger beam section or decrease the applied loads")
                logger.error(" : Design is not safe. \n ")
                logger.debug(" : =========End Of design===========")
            else:
                self.design_status = True
                self.web_plate_axial_check(self)
        else:
            self.design_status = False
            logger.warning(": Block Shear of web is less than required axial_force_w %2.2f KN" % self.axial_force_w)
            logger.info(": Select the larger section")
            logger.error(" : Design is not safe. \n ")
            logger.debug(" : =========End Of design===========")

#         ###### # capacity Check for web plate in axial = min(block, yielding, rupture)
    def web_plate_axial_check(self):
        self.axial_force_w = ((self.section.depth - (2 * self.section.flange_thickness))
                              * self.section.web_thickness * self.factored_axial_load) / (
                              self.section.area)

        A_vn_web = 2*(self.web_plate.height - (self.web_plate.bolts_one_line * self.web_bolt.dia_hole)) \
                   * self.web_plate.thickness_provided
        A_v_web = 2*self.web_plate.height * self.web_plate.thickness_provided
        self.web_plate.tension_yielding_capacity = self.tension_member_design_due_to_yielding_of_gross_section(
                                                    A_v=A_v_web, fy=self.web_plate.fy)
        self.web_plate.tension_rupture_capacity = self.tension_member_design_due_to_rupture_of_critical_section(
                                                    A_vn=A_vn_web, fu=self.web_plate.fu)

        # available_web_thickness = list([x for x in self.web_plate.thickness if ((self.web_plate.thickness_provided) <= x)])

        # for self.web_plate.thickness_provided in available_web_thickness:
        design_status_block_shear = False
        edge_dist = self.web_plate.edge_dist_provided
        end_dist = self.web_plate.end_dist_provided
        gauge = self.web_plate.gauge_provided
        pitch = self.web_plate.pitch_provided
        # print(1)

        #### Block shear capacity of web plate in axial ###

        while design_status_block_shear == False:
            Avg = 2 * ((self.web_plate.bolt_line - 1) * pitch + end_dist) * \
                  self.web_plate.thickness_provided
            Avn = 2 * ((self.web_plate.bolt_line - 1) * pitch + (
                    self.web_plate.bolt_line - 0.5) * self.web_bolt.dia_hole + end_dist) * \
                  self.web_plate.thickness_provided
            Atg = (self.web_plate.edge_dist_provided + (
                    self.web_plate.bolts_one_line - 1) * gauge) * self.web_plate.thickness_provided
            Atn = (self.web_plate.edge_dist_provided + (
                    self.web_plate.bolts_one_line - 1) * gauge - (
                           self.web_plate.bolts_one_line - 1) * self.web_bolt.dia_hole) * self.web_plate.thickness_provided

            self.web_plate.block_shear_capacity = self.block_shear_strength_section(A_vg=Avg, A_vn=Avn, A_tg=Atg,
                                                                                    A_tn=Atn,
                                                                                    f_u=self.web_plate.fu,
                                                                                    f_y=self.web_plate.fy)
            print("block_shear_strength_section",self.web_plate.block_shear_capacity )
            self.web_plate.block_shear_capacity = 2 * self.web_plate.block_shear_capacity
            if self.web_plate.block_shear_capacity < self.axial_force_w:
                if self.web_bolt.max_spacing_round >= pitch + 5 and self.web_bolt.max_end_dist_round >= end_dist + 5:  # increase thickness todo
                    if self.web_plate.bolt_line == 1:
                        end_dist += 5
                    else:
                        pitch += 5

                else:
                    break

            else:
                design_status_block_shear = True
                break

        # if design_status_block_shear == True:
        #     break
        if design_status_block_shear == True:

            self.web_plate.tension_capacity_web_plate = min( self.web_plate.tension_yielding_capacity ,
                                                             self.web_plate.tension_rupture_capacity,
                                                             self.web_plate.block_shear_capacity)
            if self.web_plate.tension_capacity_web_plate < self.axial_force_w:
                self.design_status = False
                logger.warning(": Tension capacity of web plate is less than required axial_force_w %2.2f KN" % self.axial_force_w)
                logger.info(": Select larger beam section or decrease the applied loads")
                logger.error(" : Design is not safe. \n ")
                logger.debug(" : =========End Of design===========")
            else:
                self.design_status = True
                self.web_shear_plate_check(self)
        else:
            self.design_status = False
            logger.warning(": Block Shear of web plate is less than required axial_force_w %2.2f KN" % self.axial_force_w)
            logger.info(": Increase the thickness of the plate")
            logger.error(" : Design is not safe. \n ")
            logger.debug(" : =========End Of design===========")
    def web_shear_plate_check(self):
        ###### # capacity Check for web plate  in shear = min(block, yielding, rupture)

        A_vn_web = 2 * (self.web_plate.height - (self.web_plate.bolts_one_line * self.web_bolt.dia_hole)) * \
                   self.web_plate.thickness_provided
        A_v_web = 2 * self.web_plate.height * self.web_plate.thickness_provided
        self.web_plate.shear_yielding_capacity = self.shear_yielding(
            A_v=A_v_web, fy=self.web_plate.fy)
        self.web_plate.shear_rupture_capacity = self.shear_rupture_(
            A_vn=A_vn_web, fu=self.web_plate.fu)

        available_web_thickness = list([x for x in self.web_plate.thickness if ((self.web_plate.thickness_provided) <= x)])

        # for self.web_plate.thickness_provided in available_web_thickness:  #
        design_status_block_shear = False
        edge_dist = self.web_plate.edge_dist_provided
        end_dist = self.web_plate.end_dist_provided
        gauge = self.web_plate.gauge_provided
        pitch = self.web_plate.pitch_provided

        #### Block shear capacity of web plate ###

        while design_status_block_shear == False:
            Atg = (((self.web_plate.bolt_line - 1) * self.web_plate.pitch_provided) + self.web_plate.end_dist_provided) * self.web_plate.thickness_provided
            Atn = (((self.web_plate.bolt_line - 1) * self.web_plate.pitch_provided) + ((
                        self.web_plate.bolt_line - 0.5) * self.web_bolt.dia_hole) + self.web_plate.end_dist_provided) * self.web_plate.thickness_provided
            Avg = (self.web_plate.edge_dist_provided + (
                        self.web_plate.bolts_one_line - 1) * self.web_plate.gauge_provided) * self.web_plate.thickness_provided
            Avn = ((((self.web_plate.bolts_one_line - 1)* self.web_plate.gauge_provided)
                    +self.web_plate.edge_dist_provided)- ((self.web_plate.bolts_one_line - 0.5)
                                                          * self.web_bolt.dia_hole)) *self.web_plate.thickness_provided

            self.web_plate.block_shear_capacity_shear = self.block_shear_strength_section(A_vg=Avg, A_vn=Avn, A_tg=Atg,
                                                                                    A_tn=Atn,
                                                                                    f_u=self.web_plate.fu,
                                                                                    f_y=self.web_plate.fy)
            self.web_plate.block_shear_capacity_shear = 2 * self.web_plate.block_shear_capacity_shear
            if self.web_plate.block_shear_capacity_shear < self.fact_shear_load:
                if self.web_bolt.max_spacing_round >= pitch + 5 and self.web_bolt.max_end_dist_round >= end_dist + 5:  # increase thickness todo
                    if self.web_plate.bolt_line == 1:
                        end_dist += 5
                    else:
                        pitch += 5
                else:
                    break
            else:
                design_status_block_shear = True
                break
        # if design_status_block_shear is True:
        #     break

        if design_status_block_shear is True:
            self.web_plate.shear_capacity_web_plate = min(self.web_plate.shear_yielding_capacity,
                                                          self.web_plate.shear_rupture_capacity,
                                                          self.web_plate.block_shear_capacity_shear)

            if self.web_plate.shear_capacity_web_plate  < self.fact_shear_load:
                self.design_status = False
                logger.warning(": Shear capacity of web plate is less than required fact_shear_load  %2.2f KN" % self.fact_shear_load)
                logger.info(": Select larger beam section or decrease the applied loads")
                logger.error(" : Design is not safe. \n ")
                logger.debug(" : =========End Of design===========")
            else:
                self.design_status = True
                logger.info(": Overall bolted cover plate splice connection design is safe \n")
                logger.debug(" : =========End Of design===========")
        else:
            self.design_status = False
            logger.warning(": Block Shear of web plate is less than required fact_shear_load %2.2f KN" % self.fact_shear_load)
            logger.info(": Increase the thickness of the plate")
            logger.error(" : Design is not safe. \n ")
            logger.debug(" : =========End Of design===========")

        ####todo comment out

        self.flange_plate.length = self.flange_plate.length * 2
        self.web_plate.length = self.web_plate.length * 2
        self.flange_plate.bolt_line = 2 * self.flange_plate.bolt_line
        self.flange_plate.bolts_one_line = self.flange_plate.bolts_one_line
        self.flange_plate.bolts_required = self.flange_plate.bolt_line *self.flange_plate.bolts_one_line
        self.flange_plate.midgauge = 2*(self.flange_plate.edge_dist_provided + self.section.root_radius) + \
                                     self.section.web_thickness
        self.web_plate.midpitch = (2*self.web_plate.end_dist_provided) +self.web_plate.gap
        self.flange_plate.midpitch = (2 * self.flange_plate.end_dist_provided) + self.flange_plate.gap


        self.web_plate.bolts_one_line =  self.web_plate.bolts_one_line
        self.web_plate.bolt_line = 2 * self.web_plate.bolt_line
        self.web_plate.bolts_required = self.web_plate.bolt_line * self.web_plate.bolts_one_line
        self.flange_plate.Innerlength = self.flange_plate.length

        self.min_plate_length = (((self.flange_plate.bolt_line / 2 - 1) * self.flange_bolt.min_pitch) +
                                 (2*self.flange_bolt.min_end_dist) + (self.flange_plate.gap/2))
        print("self.min_plate_length",self.min_plate_length)

        # print("anjali", self.anjali)
        print(self.section)
        print(self.load)
        print(self.flange_bolt)
        print(self.flange_plate)
        print(self.web_bolt)
        print(self.web_plate)
        print(self.web_plate.thickness_provided)
        print(self.flange_plate.thickness_provided)
        #print(design_status)
        print(self.flange_plate.length )
        print(self.web_plate.length )
        print(self.flange_plate.bolts_required )
        print(self.web_plate.bolts_required )
        print("bolt dia",self.flange_bolt.bolt_diameter_provided)
        print("flange_plate.Innerlength", self.flange_plate.Innerlength)
        print("flange_plate.Innerheight", self.flange_plate.Innerheight)
        print("flange_plate.gap", self.flange_plate.gap)
        print(self.web_plate.length)
        print("webplategap", self.web_plate.gap)

        print( "self.flange_plate.midgauge" , self.flange_plate.midgauge)
        print( "self.web_plate.midpitch" ,self.web_plate.midpitch)
        print( "self.flange_plate.midpitch" ,  self.flange_plate.midpitch)

        # if self.design_status == True:
        #
        #     logger.info(": Overall bolted cover plate splice connection design is safe \n")
        #     logger.debug(" :=========End Of design===========")
        # else:
        #     logger.error(": Design is not safe \n ")
        #     logger.debug(" :=========End Of design===========")
################################ Design Report #####################################################################################

 ################################ CAPACITY CHECK Functions#####################################################################################

    @staticmethod
    def block_shear_strength_plate(A_vg, A_vn, A_tg, A_tn, f_u, f_y):  # for flange plate
        """Calculate the block shear strength of bolted connections as per cl. 6.4.1

        Args:
            A_vg: Minimum gross area in shear along bolt line parallel to external force [in sq. mm] (float)
            A_vn: Minimum net area in shear along bolt line parallel to external force [in sq. mm] (float)
            A_tg: Minimum gross area in tension from the bolt hole to the toe of the angle,
                           end bolt line, perpendicular to the line of force, respectively [in sq. mm] (float)
            A_tn: Minimum net area in tension from the bolt hole to the toe of the angle,
                           end bolt line, perpendicular to the line of force, respectively [in sq. mm] (float)
            f_u: Ultimate stress of the plate material in MPa (float)
            f_y: Yield stress of the plate material in MPa (float)

        Return:
            block shear strength of bolted connection in N (float)

        Note:
            Reference:
            IS 800:2007, cl. 6.4.1

        """
        gamma_m0 = IS800_2007.cl_5_4_1_Table_5["gamma_m0"]['yielding']
        gamma_m1 = IS800_2007.cl_5_4_1_Table_5["gamma_m1"]['ultimate_stress']
        T_db1 = A_vg * f_y / (math.sqrt(3) * gamma_m0) + 0.9 * A_tn * f_u / gamma_m1
        T_db2 = 0.9 * A_vn * f_u / (math.sqrt(3) * gamma_m1) + A_tg * f_y / gamma_m0
        Tdb = min(T_db1, T_db2)
        Tdb = round(Tdb , 3)
        return Tdb

        # Function for block shear capacity calculation

    @staticmethod
    def block_shear_strength_section(A_vg, A_vn, A_tg, A_tn, f_u, f_y):
        """Calculate the block shear strength of bolted connections as per cl. 6.4.1

        Args:
            A_vg: Minimum gross area in shear along bolt line parallel to external force [in sq. mm] (float)
            A_vn: Minimum net area in shear along bolt line parallel to external force [in sq. mm] (float)
            A_tg: Minimum gross area in tension from the bolt hole to the toe of the angle,
                           end bolt line, perpendicular to the line of force, respectively [in sq. mm] (float)
            A_tn: Minimum net area in tension from the bolt hole to the toe of the angle,
                           end bolt line, perpendicular to the line of force, respectively [in sq. mm] (float)
            f_u: Ultimate stress of the plate material in MPa (float)
            f_y: Yield stress of the plate material in MPa (float)

        Return:
            block shear strength of bolted connection in N (float)

        Note:
            Reference:
            IS 800:2007, cl. 6.4.1

        """
        gamma_m0 = IS800_2007.cl_5_4_1_Table_5["gamma_m0"]['yielding']
        gamma_m1 = IS800_2007.cl_5_4_1_Table_5["gamma_m1"]['ultimate_stress']
        T_db1 = A_vg * f_y / (math.sqrt(3) * gamma_m0) + 0.9 * A_tn * f_u / gamma_m1
        T_db2 = 0.9 * A_vn * f_u / (math.sqrt(3) * gamma_m1) + A_tg * f_y / gamma_m0
        Tdb = min(T_db1, T_db2)
        Tdb = round(Tdb , 2)
        return Tdb
        # cl 6.2 Design Strength Due to Yielding of Gross Section

    @staticmethod
    def tension_member_design_due_to_yielding_of_gross_section(A_v, fy):
        '''
             Args:
                 A_v (float) Area under shear
                 Beam_fy (float) Yield stress of Beam material
             Returns:
                 Capacity of Beam web in shear yielding
             '''
        gamma_m0 = IS800_2007.cl_5_4_1_Table_5["gamma_m0"]['yielding']
        # A_v = height * thickness
        tdg = (A_v * fy) / (gamma_m0 )
        return tdg

    @staticmethod
    def tension_member_design_due_to_rupture_of_critical_section(A_vn, fu):
        '''
               Args:
                   A_vn (float) Net area under shear
                   Beam_fu (float) Ultimate stress of Beam material
               Returns:
                   Capacity of beam web in shear rupture
               '''

        gamma_m1 = IS800_2007.cl_5_4_1_Table_5["gamma_m1"]['ultimate_stress']
        # A_vn = (height- bolts_one_line * dia_hole) * thickness
        T_dn = 0.9 * A_vn * fu / (gamma_m1)
        return T_dn

    @staticmethod
    def shear_yielding(A_v,fy):
        '''
        Args:
            length (float) length of member in direction of shear load
            thickness(float) thickness of member resisting shear
            beam_fy (float) Yeild stress of section material
        Returns:
            Capacity of section in shear yeiding
        '''

        # A_v = length * thickness
        gamma_m0 = 1.1
        # print(length, thickness, fy, gamma_m0)
        # V_p = (0.6 * A_v * fy) / (math.sqrt(3) * gamma_m0 * 1000)  # kN
        V_p = (A_v * fy) / (math.sqrt(3) * gamma_m0 )  # N
        return V_p

    @staticmethod
    def shear_rupture_(A_vn, fu):
        '''
               Args:
                   A_vn (float) Net area under shear
                   Beam_fu (float) Ultimate stress of Beam material
               Returns:
                   Capacity of beam web in shear rupture
               '''

        gamma_m1 = IS800_2007.cl_5_4_1_Table_5["gamma_m1"]['ultimate_stress']
        # A_vn = (height- bolts_one_line * dia_hole) * thickness
        T_dn = 0.9 * A_vn * fu / (math.sqrt(3) *gamma_m1)
        return T_dn
    #
    # def web_force(column_d, column_f_t, column_t_w, axial_force, column_area):
    #     """
    #     Args:
    #        c_d: Overall depth of the column section in mm (float)
    #        column_f_t: Thickness of flange in mm (float)
    #        column_t_w: Thickness of flange in mm (float)
    #        axial_force: Factored axial force in kN (float)
    #
    #     Returns:
    #         Force in flange in kN (float)
    #     """
    #     axial_force_w = int(
    #         ((column_d - 2 * (column_f_t)) * column_t_w * axial_force ) / column_area)   # N
    #     return round(axial_force_w)

    @staticmethod
    def limiting_width_thk_ratio(column_f_t, column_t_w, D, column_b, column_fy, factored_axial_force,
                                 column_area, compression_element, section):
        column_d = D - (2 * column_f_t)
        epsilon = float(math.sqrt(250 / column_fy))
        axial_force_w = int(
            ((D - 2 * (column_f_t)) * column_t_w * factored_axial_force) / (column_area))  # N

        des_comp_stress_web = column_fy
        des_comp_stress_section = column_fy
        avg_axial_comp_stress = axial_force_w / ((D - 2 * column_f_t) * column_t_w)
        r1 = avg_axial_comp_stress / des_comp_stress_web
        r2 = avg_axial_comp_stress / des_comp_stress_section
        a = column_b / column_f_t
        # column_d = D - 2(column_f_t)
        # compression_element=["External","Internal","Web of an I-H" ,"box section" ]
        # section=["rolled","welded","compression due to bending","generally", "Axial compression" ]
        # section = "rolled"
        if compression_element == "External" or compression_element == "Internal":
            if section == "Rolled":
                if column_b * 0.5 / column_f_t <= 9.4 * epsilon:
                    class_of_section1 = "plastic"
                elif column_b * 0.5 / column_f_t <= 10.5 * epsilon:
                    class_of_section1 = "compact"
                elif column_b * 0.5 / column_f_t <= 15.7 * epsilon:
                    class_of_section1 = "semi-compact"
                # else:
                #     print('fail')
                # print("class_of_section", class_of_section )
            elif section == "welded":
                if column_b * 0.5 / column_f_t <= 8.4 * epsilon:
                    class_of_section1 = "plastic"
                elif column_b * 0.5 / column_f_t <= 9.4 * epsilon:
                    class_of_section1 = "compact"
                elif column_b * 0.5 / column_f_t <= 13.6 * epsilon:
                    class_of_section1 = "semi-compact"
                # else:
                #     print('fail')
            elif section == "compression due to bending":
                if column_b * 0.5 / column_f_t <= 29.3 * epsilon:
                    class_of_section1 = "plastic"
                elif column_b * 0.5 / column_f_t <= 33.5 * epsilon:
                    class_of_section1 = "compact"
                elif column_b * 0.5 / column_f_t <= 42 * epsilon:
                    class_of_section1 = "semi-compact"
                # else:
                #     print('fail')
            # else:
            #     pass

        elif compression_element == "Web of an I-H" or compression_element == "box section":
            if section == "generally":
                if r1 < 0:
                    if column_d / column_t_w <= max((84 * epsilon / (1 + r1)), (42 * epsilon)):
                        class_of_section1 = "plastic"
                    elif column_d / column_t_w <= (max(105 * epsilon / (1 + r1)), (42 * epsilon)):
                        class_of_section1 = "compact"
                    elif column_d / column_t_w <= max((126 * epsilon / (1 + 2 * r2)), column_d / column_t_w >= (
                            42 * epsilon)):
                        class_of_section1 = "semi-compact"
                    # else:
                    #     print('fail')
                    # print("class_of_section3", class_of_section)
                elif r1 > 0:
                    if column_d / column_t_w <= max((84 * epsilon / (1 + r1)), (42 * epsilon)):
                        class_of_section1 = "plastic"
                    elif column_d / column_t_w <= max((105 * epsilon / (1 + (r1 * 1.5))), (
                            42 * epsilon)):
                        class_of_section1 = "compact"
                    elif column_d / column_t_w <= max((126 * epsilon / (1 + 2 * r1)), (
                            42 * epsilon)):
                        class_of_section1 = "semi-compact"

            elif section == "Axial compression":
                if column_d / column_t_w <= (42 * epsilon):
                    class_of_section1 = "semi-compact"
                else:
                    class_of_section1 = "N/A"

        print("class_of_section", class_of_section1)
        if class_of_section1 == "plastic":
            class_of_section1 = 1
        elif class_of_section1 == "compact":
            class_of_section1 = 2
        elif class_of_section1 == "semi-compact":
            class_of_section1 = 3
        # else:
        #     print('fail')
        print("class_of_section2", class_of_section1)

        return class_of_section1

        print("class_of_section1", class_of_section1)

    def min_thick_based_on_area(self, tk, width, list_of_pt_tk, t_w, r_1, D,
                                preference=None):  # area of flange plate should be greater than 1.05 times area of flange
        # 20 is the maximum spacing either side of the plate
        self.flange_crs_sec_area = tk * width
        self.design_status = True
        for y in list_of_pt_tk:
            if preference != None:
                if preference == "Outside":
                    outerwidth = width
                    self.flange_plate_crs_sec_area = y * width
                    if self.flange_plate_crs_sec_area >= self.flange_crs_sec_area * 1.05:
                        thickness = y
                        self.design_status = True
                        break
                    else:
                        thickness = 0
                        self.design_status = False

                elif preference == "Outside + Inside":
                    self.outerwidth = width
                    self.innerwidth = (width - t_w - (2 * r_1)) / 2
                    if self.innerwidth < 50:
                        # logger.error(":Inner Plate not possible")
                        self.design_status = False
                        thickness = 0
                    else:
                        self.design_status = True
                        self.flange_plate_crs_sec_area = (self.outerwidth + (2*self.innerwidth)) * y
                        if self.flange_plate_crs_sec_area >= self.flange_crs_sec_area * 1.05:
                            thickness = y
                            self.design_status = True
                            break
                        else:
                            thickness = 0
                            self.design_status = False

            else:
                self.webwidth = D - (2 * tk) - (2 * r_1)
                self.web_crs_area = t_w * self.webwidth
                self.web_plate_crs_sec_area = 2 * self.webwidth * y
                if self.web_plate_crs_sec_area  >= self.web_crs_area * 1.05:
                    thickness = y
                    self.design_status = True
                    break
                else:
                    thickness = 0
                    self.design_status = False

        return thickness


    def call_3DModel(self,ui,bgcolor):
        # Call to calculate/create the BB Cover Plate Bolted CAD model
        # status = self.resultObj['Bolt']['status']
        # if status is True:
        #     self.createBBCoverPlateBoltedCAD()
        #     self.ui.btn3D.setChecked(Qt.Checked)
        if ui.btn3D.isChecked():
            ui.chkBxBeam.setChecked(Qt.Unchecked)
            ui.chkBxFinplate.setChecked(Qt.Unchecked)
            ui.mytabWidget.setCurrentIndex(0)

        # Call to display the BB Cover Plate Bolted CAD model
        #     ui.Commondisplay_3DModel("Model", bgcolor)  # "gradient_bg")
        ui.commLogicObj.display_3DModel("Model",bgcolor)

        # else:
        #     self.display.EraseAll()

    def call_3DBeam(self, ui, bgcolor):
        # status = self.resultObj['Bolt']['status']
        # if status is True:
        #     self.ui.chkBx_beamSec1.setChecked(Qt.Checked)
        if ui.chkBxBeam.isChecked():
            ui.btn3D.setChecked(Qt.Unchecked)
            ui.chkBxBeam.setChecked(Qt.Unchecked)
            ui.mytabWidget.setCurrentIndex(0)
        # self.display_3DModel("Beam", bgcolor)
        ui.commLogicObj.display_3DModel("Beam",bgcolor)


    def call_3DConnector(self, ui, bgcolor):
        # status = self.resultObj['Bolt']['status']
        # if status is True:
        #     self.ui.chkBx_extndPlate.setChecked(Qt.Checked)
        if ui.chkBxFinplate.isChecked():
            ui.btn3D.setChecked(Qt.Unchecked)
            ui.chkBxBeam.setChecked(Qt.Unchecked)
            ui.mytabWidget.setCurrentIndex(0)
        # self.display_3DModel("Connector", bgcolor)
        ui.commLogicObj.display_3DModel("Connector", bgcolor)

    ################################ Design Report #####################################################################################

    def save_design(self, popup_summary):
        # bolt_list = str(*self.bolt.bolt_diameter, sep=", ")
        self.report_supporting = {KEY_DISP_SEC_PROFILE: "ISection",
                                  KEY_DISP_BEAMSEC: self.section.designation,
                                  KEY_DISP_FLANGESPLATE_PREFERENCES: self.preference,
                                  KEY_DISP_MATERIAL: self.section.material,
                                  KEY_DISP_FU: self.section.fu,
                                  KEY_DISP_FY: self.section.fy,
                                  'Mass': self.section.mass,
                                  'Area(mm2) - A': round(self.section.area, 2),
                                  'D(mm)': self.section.depth,
                                  'B(mm)': self.section.flange_width,
                                  't(mm)': self.section.web_thickness,
                                  'T(mm)': self.section.flange_thickness,
                                  'FlangeSlope': self.section.flange_slope,
                                  'R1(mm)': self.section.root_radius,
                                  'R2(mm)': self.section.toe_radius,
                                  'Iz(mm4)': self.section.mom_inertia_z,
                                  'Iy(mm4)': self.section.mom_inertia_y,
                                  'rz(mm)': self.section.rad_of_gy_z,
                                  'ry(mm)': self.section.rad_of_gy_y,
                                  'Zz(mm3)': self.section.elast_sec_mod_z,
                                  'Zy(mm3)': self.section.elast_sec_mod_y,
                                  'Zpz(mm3)': self.section.plast_sec_mod_z,
                                  'Zpy(mm3)': self.section.elast_sec_mod_y}

        self.report_input = \
            {KEY_MODULE: self.module,
             KEY_MAIN_MODULE: self.mainmodule,
             # KEY_CONN: self.connectivity,
             KEY_DISP_MOMENT: self.load.moment,
             KEY_DISP_SHEAR: self.load.shear_force,
             KEY_DISP_AXIAL: self.load.axial_force,

             "Section": "TITLE",
             "Section Details": self.report_supporting,

             "Bolt Details": "TITLE",
             KEY_DISP_D: str(self.bolt.bolt_diameter),
             KEY_DISP_GRD: str(self.bolt.bolt_grade),
             KEY_DISP_TYP: self.bolt.bolt_type,

             KEY_BOLT_FU:  self.flange_bolt.bolt_fu,
             KEY_BOLT_FY: round(self.flange_bolt.bolt_fy,2),

             KEY_DISP_DP_BOLT_HOLE_TYPE: self.bolt.bolt_hole_type,
             KEY_DISP_DP_BOLT_SLIP_FACTOR: self.bolt.mu_f,
             KEY_DISP_DP_DETAILING_EDGE_TYPE: self.bolt.edge_type,
             KEY_DISP_DP_DETAILING_GAP: self.flange_plate.gap,
             KEY_DISP_DP_DETAILING_CORROSIVE_INFLUENCES: self.bolt.corrosive_influences}


        self.report_check = []

        #####Outer plate#####
        flange_connecting_plates = [self.flange_plate.thickness_provided, self.section.flange_thickness]

        flange_bolt_shear_capacity_kn = round(self.flange_bolt.bolt_shear_capacity / 1000, 2)
        # flange_bolt_bearing_capacity_kn = round(self.flange_bolt.bolt_bearing_capacity / 1000, 2)
        flange_bolt_capacity_kn = round(self.flange_bolt.bolt_capacity / 1000, 2)
        flange_kb_disp = round(self.flange_bolt.kb, 2)
        flange_kh_disp = round(self.flange_bolt.kh, 2)
        flange_bolt_force_kn = round(self.flange_plate.bolt_force, 2)
        flange_bolt_capacity_red_kn = round(self.flange_plate.bolt_capacity_red, 2)
        if self.member_capacity_status == True and self.initial_pt_thk_status == True:
            self.thick_f = self.flange_plate.thickness_provided
            self.thick_w = self.web_plate.thickness_provided
        else:
            self.thick_f = self.max_thick_f
            self.thick_w = self.max_thick_w
        ########Inner plate#####
        innerflange_connecting_plates = [self.flange_plate.thickness_provided, self.section.flange_thickness]

        innerflange_bolt_shear_capacity_kn = round(self.flange_bolt.bolt_shear_capacity / 1000, 2)

        innerflange_bolt_capacity_kn = round(self.flange_bolt.bolt_capacity / 1000, 2)
        innerflange_kb_disp = round(self.flange_bolt.kb, 2)
        innerflange_kh_disp = round(self.flange_bolt.kh, 2)
        innerflange_bolt_force_kn = round(self.flange_plate.bolt_force, 2)
        innerflange_bolt_capacity_red_kn = round(self.flange_plate.bolt_capacity_red, 2)
        min_plate_length = (((self.flange_plate.bolt_line / 2 - 1) * self.flange_bolt.min_pitch) + (
                2 * self.flange_bolt.min_end_dist) + (self.flange_plate.gap / 2))
        h = self.section.depth - (2 * self.section.flange_thickness)
        self.Pmc = self.section.plastic_moment_capactiy
        self.Mdc = self.section.moment_d_def_criteria

        t1 = ('SubSection', 'Member Capacity', '|p{4cm}|p{5cm}|p{5.5cm}|p{1.5cm}|')
        self.report_check.append(t1)
        gamma_m0 = IS800_2007.cl_5_4_1_Table_5["gamma_m0"]['yielding']
        t1 = (KEY_OUT_DISP_AXIAL_CAPACITY, '', axial_capacity(area=self.section.area,
                                                              fy=self.section.fy,
                                                              gamma_m0=gamma_m0,
                                                              axial_capacity=round(self.axial_capacity / 1000, 2)), '')
        self.report_check.append(t1)

        self.shear_capacity1 = round(((self.section.depth - (2 * self.section.flange_thickness)) *
                                      self.section.web_thickness * self.section.fy) / (math.sqrt(3) * gamma_m0), 2)

        t1 = (KEY_OUT_DISP_SHEAR_CAPACITY, '', shear_capacity(h=h, t=self.section.web_thickness,
                                                              f_y=self.section.fy, gamma_m0=gamma_m0,
                                                              shear_capacity=round(self.shear_capacity1 / 1000, 2)), '')
        self.report_check.append(t1)
        t1 = (KEY_OUT_DISP_PLASTIC_MOMENT_CAPACITY, '', plastic_moment_capacty(beta_b=self.beta_b,
                                                                               Z_p=self.Z_p, f_y=self.section.fy,
                                                                               gamma_m0=gamma_m0,
                                                                               Pmc=round(self.Pmc / 1000000, 2)), '')
        self.report_check.append(t1)

        t1 = (KEY_OUT_DISP_MOMENT_D_DEFORMATION, '', moment_d_deformation_criteria(fy=self.section.fy,
                                                                                   Z_e=self.section.elast_sec_mod_z,
                                                                                   Mdc=round(self.Mdc / 1000000, 2)),
              '')
        self.report_check.append(t1)

        t1 = (KEY_OUT_DISP_MOMENT_CAPACITY, '', moment_capacity(Pmc=round(self.Pmc / 1000000, 2),
                                                                Mdc=round(self.Mdc / 1000000, 2),
                                                                M_c=round(self.section.moment_capacity / 1000000, 2)),
              '')
        self.report_check.append(t1)

        t1 = ('SubSection', 'Load Considered', '|p{4cm}|p{5cm}|p{5.5cm}|p{1.5cm}|')
        self.report_check.append(t1)
        t1 = (KEY_DISP_APPLIED_AXIAL_FORCE, min_max_axial_capacity(axial_capacity=round(self.axial_capacity / 1000, 2),
                                                               min_ac=round(self.min_axial_load / 1000, 2)),
              prov_axial_load(axial_input=self.load.axial_force,
                              min_ac=round(self.min_axial_load / 1000, 2),
                              app_axial_load=round(self.factored_axial_load / 1000, 2)),
              get_pass_fail(self.min_axial_load / 1000,
                            self.factored_axial_load / 1000, relation='lesser'))
        self.report_check.append(t1)
        t1 = (KEY_DISP_APPLIED_SHEAR_LOAD, min_max_shear_capacity(shear_capacity=round(self.shear_capacity1 / 1000, 2),
                                                              min_sc=round(self.shear_load1 / 1000, 2)),
              prov_shear_load(shear_input=self.load.shear_force,
                              min_sc=round(self.shear_load1 / 1000, 2),
                              app_shear_load=round(self.fact_shear_load / 1000, 2)),
              get_pass_fail(self.shear_load1 / 1000,
                            self.fact_shear_load / 1000, relation='lesser'))
        self.report_check.append(t1)

        t1 = (KEY_DISP_APPLIED_MOMENT_LOAD,
              min_max_moment_capacity(moment_capacity=round(self.section.moment_capacity / 1000000, 2),
                                  min_mc=round(self.load_moment_min / 1000000, 2)),
              prov_moment_load(moment_input=self.load.moment,
                               min_mc=round(self.load_moment_min / 1000000, 2),
                               app_moment_load=round(self.load_moment / 1000000, 2)),
              get_pass_fail(round(self.load_moment_min / 1000000, 2),
                            round(self.load_moment / 1000000, 2), relation="lesser"))
        self.report_check.append(t1)

        t23 = (KEY_OUT_DISP_FORCES_WEB, '', forces_in_web(Au=round(self.factored_axial_load / 1000, 2),
                                                          T=self.section.flange_thickness, A=self.section.area,
                                                          t=self.section.web_thickness, D=self.section.depth,
                                                          Zw=self.Z_p, Mu=round(self.load_moment / 1000000, 2),
                                                          Z=self.section.plast_sec_mod_z,
                                                          Mw=round(self.moment_web / 1000000, 2),
                                                          Aw=round(self.axial_force_w / 1000, 2)), '')
        self.report_check.append(t23)

        t23 = (KEY_OUT_DISP_FORCES_FLANGE, '', forces_in_flange(Au=round(self.factored_axial_load / 1000, 2),
                                                                B=self.section.flange_width,
                                                                T=self.section.flange_thickness, A=self.section.area,
                                                                D=self.section.depth,
                                                                Mu=round(self.load_moment / 1000000, 2),
                                                                Mw=round(self.moment_web / 1000000, 2),
                                                                Mf=round(self.moment_flange / 1000000, 2),
                                                                Af=round(self.axial_force_f / 1000, 2),
                                                                ff=round(self.flange_force / 1000, 2), ), '')
        self.report_check.append(t23)

        t1 = ('SubSection', 'Flange Bolt Checks', '|p{4cm}|p{5cm}|p{5.5cm}|p{1.5cm}|')
        self.report_check.append(t1)

        t6 = (KEY_OUT_DISP_D_PROVIDED, "Bolt Quantity Optimisation", display_prov(self.bolt.bolt_diameter_provided, "d"), '')

        self.report_check.append(t6)

        t8 = (KEY_OUT_DISP_GRD_PROVIDED, "Bolt Grade Optimisation", self.bolt.bolt_grade_provided, '')
        self.report_check.append(t8)

        t8 = (KEY_DISP_BOLT_HOLE, " ", display_prov(self.flange_bolt.dia_hole, "d_0"), '')
        self.report_check.append(t8)

        if self.preference == "Outside":
            if self.flange_bolt.bolt_type == TYP_BEARING:
                flange_bolt_bearing_capacity_kn = round(self.flange_bolt.bolt_bearing_capacity / 1000, 2)
                t1 = (KEY_OUT_DISP_FLANGE_BOLT_SHEAR, '', bolt_shear_prov(self.flange_bolt.bolt_fu, 1,
                                                                          self.flange_bolt.bolt_net_area,
                                                                          self.flange_bolt.gamma_mb,
                                                                          flange_bolt_shear_capacity_kn), '')
                self.report_check.append(t1)
                t2 = (KEY_OUT_DISP_FLANGE_BOLT_BEARING, '', bolt_bearing_prov(flange_kb_disp,
                                                                              self.bolt.bolt_diameter_provided,
                                                                              self.bolt_conn_plates_t_fu_fy,
                                                                              self.flange_bolt.gamma_mb,
                                                                              flange_bolt_bearing_capacity_kn), '')
                self.report_check.append(t2)
                t3 = (KEY_OUT_DISP_FLANGE_BOLT_CAPACITY, '', bolt_capacity_prov(flange_bolt_shear_capacity_kn,
                                                                                flange_bolt_bearing_capacity_kn,
                                                                                flange_bolt_capacity_kn), '')
                self.report_check.append(t3)
            else:

                t4 = (KEY_OUT_DISP_FLANGE_BOLT_SLIP, '', HSFG_bolt_capacity_prov(mu_f=self.bolt.mu_f, n_e=1,
                                                                                 K_h=flange_kh_disp,
                                                                                 fub=self.flange_bolt.bolt_fu,
                                                                                 Anb=self.bolt.bolt_net_area,
                                                                                 gamma_mf=self.web_bolt.gamma_mf,
                                                                                 capacity=flange_bolt_capacity_kn), '')
                self.report_check.append(t4)
        else:
            if self.flange_bolt.bolt_type == TYP_BEARING:
                innerflange_bolt_bearing_capacity_kn = round(self.flange_bolt.bolt_bearing_capacity / 1000, 2)
                t1 = (KEY_OUT_DISP_FLANGE_BOLT_SHEAR, '', bolt_shear_prov(self.flange_bolt.bolt_fu, 2,
                                                                          self.flange_bolt.bolt_net_area,
                                                                          self.flange_bolt.gamma_mb,
                                                                          innerflange_bolt_shear_capacity_kn), '')
                self.report_check.append(t1)
                t2 = (KEY_OUT_DISP_FLANGE_BOLT_BEARING, '', bolt_bearing_prov(innerflange_kb_disp,
                                                                              self.bolt.bolt_diameter_provided,
                                                                              self.bolt_conn_plates_t_fu_fy,
                                                                              self.flange_bolt.gamma_mb,
                                                                              innerflange_bolt_bearing_capacity_kn), '')
                self.report_check.append(t2)
                t3 = (KEY_OUT_DISP_FLANGE_BOLT_CAPACITY, '', bolt_capacity_prov(innerflange_bolt_shear_capacity_kn,
                                                                                innerflange_bolt_bearing_capacity_kn,
                                                                                innerflange_bolt_capacity_kn), '')
                self.report_check.append(t3)
            else:

                t4 = (KEY_OUT_DISP_FLANGE_BOLT_SLIP, '', HSFG_bolt_capacity_prov(mu_f=self.bolt.mu_f, n_e=1,
                                                                                 K_h=innerflange_kh_disp,
                                                                                 fub=self.flange_bolt.bolt_fu,
                                                                                 Anb=self.bolt.bolt_net_area,
                                                                                 gamma_mf=self.web_bolt.gamma_mf,
                                                                                 capacity=innerflange_bolt_capacity_kn),
                      '')
                self.report_check.append(t4)

        t6 = (DISP_NUM_OF_BOLTS, get_trial_bolts(V_u=0.0, A_u=(round(self.flange_force / 1000, 2)),
                                                 bolt_capacity=flange_bolt_capacity_kn, multiple=2),
              self.flange_plate.bolts_required, '')
        self.report_check.append(t6)

        t6 = (DISP_NUM_OF_COLUMNS, '', display_prov(self.flange_plate.bolt_line, "n_c"), '')

        self.report_check.append(t6)
        t7 = (DISP_NUM_OF_ROWS, '', display_prov(self.flange_plate.bolts_one_line, "n_r"), '')
        self.report_check.append(t7)
        t1 = (DISP_MIN_PITCH, min_pitch(self.bolt.bolt_diameter_provided),
              self.flange_plate.pitch_provided,
              get_pass_fail(self.flange_bolt.min_pitch, self.flange_plate.pitch_provided, relation='lesser'))
        self.report_check.append(t1)
        t1 = (DISP_MAX_PITCH, max_pitch(flange_connecting_plates),
              self.flange_plate.pitch_provided,
              get_pass_fail(self.flange_bolt.max_spacing, self.flange_plate.pitch_provided, relation='greater'))
        self.report_check.append(t1)
        t2 = (DISP_MIN_GAUGE, min_pitch(self.bolt.bolt_diameter_provided),
              self.flange_plate.gauge_provided,
              get_pass_fail(self.flange_bolt.min_gauge, self.flange_plate.gauge_provided, relation="lesser"))
        self.report_check.append(t2)
        t2 = (DISP_MAX_GAUGE, max_pitch(flange_connecting_plates),
              self.flange_plate.gauge_provided,
              get_pass_fail(self.flange_bolt.max_spacing, self.flange_plate.gauge_provided, relation="greater"))
        self.report_check.append(t2)
        t3 = (DISP_MIN_END, min_edge_end(self.flange_bolt.dia_hole, self.bolt.edge_type),
              self.flange_plate.end_dist_provided,
              get_pass_fail(self.flange_bolt.min_end_dist, self.flange_plate.end_dist_provided, relation='lesser'))
        self.report_check.append(t3)
        t4 = (DISP_MAX_END, max_edge_end(self.flange_plate.fy, self.flange_plate.thickness_provided),
              self.flange_plate.end_dist_provided,
              get_pass_fail(self.flange_bolt.max_end_dist, self.flange_plate.end_dist_provided, relation='greater'))
        self.report_check.append(t4)
        t3 = (DISP_MIN_EDGE, min_edge_end(self.flange_bolt.dia_hole, self.bolt.edge_type),
              self.flange_plate.edge_dist_provided,
              get_pass_fail(self.flange_bolt.min_edge_dist, self.flange_plate.edge_dist_provided, relation='lesser'))
        self.report_check.append(t3)
        t4 = (DISP_MAX_EDGE, max_edge_end(self.flange_plate.fy, self.flange_plate.thickness_provided),
              self.flange_plate.edge_dist_provided,
              get_pass_fail(self.flange_bolt.max_edge_dist, self.flange_plate.edge_dist_provided, relation="greater"))
        self.report_check.append(t4)

        t10 = (KEY_OUT_LONG_JOINT, long_joint_bolted_req(),
               long_joint_bolted_prov(self.flange_plate.bolt_line, self.flange_plate.bolts_one_line,
                                      self.flange_plate.pitch_provided,
                                      self.flange_plate.gauge_provided, self.bolt.bolt_diameter_provided,
                                      flange_bolt_capacity_kn,
                                      flange_bolt_capacity_red_kn), "")
        self.report_check.append(t10)

        web_connecting_plates = [self.web_plate.thickness_provided, self.section.web_thickness]

        web_bolt_shear_capacity_kn = round(self.web_bolt.bolt_shear_capacity / 1000, 2)
        # web_bolt_bearing_capacity_kn = round(self.web_bolt.bolt_bearing_capacity / 1000, 2)
        web_bolt_capacity_kn = round(self.web_bolt.bolt_capacity / 1000, 2)
        web_kb_disp = round(self.web_bolt.kb, 2)
        web_kh_disp = round(self.web_bolt.kh, 2)

        web_bolt_force_kn = round(self.web_plate.bolt_force / 1000, 2)
        web_bolt_capacity_red_kn = round(self.web_plate.bolt_capacity_red / 1000, 2)
        res_force = self.web_plate.bolt_force * self.web_plate.bolt_line * self.web_plate.bolts_one_line
        print("res_focce", res_force)

        t1 = ('SubSection', 'Web Bolt Checks', '|p{4cm}|p{5cm}|p{5.5cm}|p{1.5cm}|')
        self.report_check.append(t1)
        if self.flange_bolt.bolt_type == TYP_BEARING:
            web_bolt_bearing_capacity_kn = round(self.web_bolt.bolt_bearing_capacity / 1000, 2)
            t1 = (KEY_OUT_DISP_WEB_BOLT_SHEAR, '', bolt_shear_prov(self.web_bolt.bolt_fu, 2,
                                                                   self.web_bolt.bolt_net_area,
                                                                   self.web_bolt.gamma_mb,
                                                                   web_bolt_shear_capacity_kn), '')
            self.report_check.append(t1)
            t2 = (KEY_OUT_DISP_WEB_BOLT_BEARING, '', bolt_bearing_prov(web_kb_disp,
                                                                       self.bolt.bolt_diameter_provided,
                                                                       self.bolt_conn_plates_web_t_fu_fy,
                                                                       self.web_bolt.gamma_mb,
                                                                       web_bolt_bearing_capacity_kn), '')
            self.report_check.append(t2)
            t3 = (KEY_OUT_DISP_WEB_BOLT_CAPACITY, '', bolt_capacity_prov(web_bolt_shear_capacity_kn,
                                                                         web_bolt_bearing_capacity_kn,
                                                                         web_bolt_capacity_kn), '')
            self.report_check.append(t3)
        else:

            t4 = (KEY_OUT_DISP_WEB_BOLT_SLIP, '', HSFG_bolt_capacity_prov(mu_f=self.bolt.mu_f, n_e=1,
                                                                          K_h=web_kh_disp, fub=self.web_bolt.bolt_fu,
                                                                          Anb=self.web_bolt.bolt_net_area,
                                                                          gamma_mf=self.web_bolt.gamma_mf,
                                                                          capacity=web_bolt_capacity_kn), '')
            self.report_check.append(t4)

        t5 = (DISP_NUM_OF_BOLTS, get_trial_bolts(V_u=round(self.fact_shear_load / 1000, 2),
                                                 A_u=(round(self.axial_force_w / 1000, 2)),
                                                 bolt_capacity=web_bolt_capacity_kn, multiple=2),
              self.web_plate.bolts_required, '')
        self.report_check.append(t5)  # todo no of bolts
        # t5 = (DISP_NUM_OF_BOLTS, get_trial_bolts(self.load.shear_force, self.load.axial_force, bolt_capacity_kn),
        #     display_prov(self.plate.bolts_required, "n"), '')
        # self.report_check.append(t5)
        t6 = (DISP_NUM_OF_COLUMNS, '', display_prov(self.web_plate.bolt_line, "n_c"), '')

        self.report_check.append(t6)
        t7 = (DISP_NUM_OF_ROWS, '', display_prov(self.web_plate.bolts_one_line, "n_r"), '')
        self.report_check.append(t7)

        t1 = (DISP_MIN_PITCH, min_pitch(self.bolt.bolt_diameter_provided),
              self.web_plate.pitch_provided,
              get_pass_fail(self.web_bolt.min_pitch, self.web_plate.pitch_provided, relation='lesser'))
        self.report_check.append(t1)
        t1 = (DISP_MAX_PITCH, max_pitch(web_connecting_plates),
              self.web_plate.pitch_provided,
              get_pass_fail(self.web_bolt.max_spacing, self.web_plate.pitch_provided,
                            relation='greater'))
        self.report_check.append(t1)
        t2 = (DISP_MIN_GAUGE, min_pitch(self.bolt.bolt_diameter_provided),
              self.web_plate.gauge_provided,
              get_pass_fail(self.web_bolt.min_gauge, self.web_plate.gauge_provided, relation="lesser"))
        self.report_check.append(t2)
        t2 = (DISP_MAX_GAUGE, max_pitch(web_connecting_plates),
              self.web_plate.gauge_provided,
              get_pass_fail(self.flange_bolt.max_spacing, self.web_plate.gauge_provided,
                            relation="greater"))
        self.report_check.append(t2)
        t3 = (DISP_MIN_END, min_edge_end(self.web_bolt.dia_hole, self.bolt.edge_type),
              self.web_plate.end_dist_provided,
              get_pass_fail(self.web_bolt.min_end_dist, self.web_plate.end_dist_provided,
                            relation='lesser'))
        self.report_check.append(t3)
        t4 = (DISP_MAX_END, max_edge_end(self.web_plate.fy, self.web_plate.thickness_provided),
              self.web_plate.end_dist_provided,
              get_pass_fail(self.web_bolt.max_end_dist, self.web_plate.end_dist_provided,
                            relation='greater'))
        self.report_check.append(t4)
        t3 = (DISP_MIN_EDGE, min_edge_end(self.web_bolt.dia_hole, self.bolt.edge_type),
              self.web_plate.edge_dist_provided,
              get_pass_fail(self.web_bolt.min_edge_dist, self.web_plate.edge_dist_provided,
                            relation='lesser'))
        self.report_check.append(t3)
        t4 = (DISP_MAX_EDGE, max_edge_end(self.web_plate.fy, self.web_plate.thickness_provided),
              self.web_plate.edge_dist_provided,
              get_pass_fail(self.web_bolt.max_edge_dist, self.web_plate.edge_dist_provided,
                            relation="greater"))
        self.report_check.append(t4)

        t10 = (KEY_OUT_REQ_PARA_BOLT, '', parameter_req_bolt_force(bolts_one_line=self.web_plate.bolts_one_line
                                                                   , gauge=self.web_plate.gauge_provided,
                                                                   ymax=round(self.web_plate.ymax, 2),
                                                                   xmax=round(self.web_plate.xmax, 2),
                                                                   bolt_line=self.web_plate.bolt_line,
                                                                   pitch=self.web_plate.pitch_provided,
                                                                   length_avail=self.web_plate.length_avail), '')
        self.report_check.append(t10)

        t10 = (KEY_OUT_REQ_MOMENT_DEMAND_BOLT, '', moment_demand_req_bolt_force(
            shear_load=round(self.fact_shear_load / 1000, 2),
            web_moment=round(self.moment_web / 1000000, 2), ecc=self.web_plate.ecc,
            moment_demand=round(self.web_plate.moment_demand / 1000000, 2)), '')

        self.report_check.append(t10)

        t10 = (KEY_OUT_BOLT_FORCE, '', Vres_bolts(bolts_one_line=self.web_plate.bolts_one_line,
                                                  ymax=round(self.web_plate.ymax, 2),
                                                  xmax=round(self.web_plate.xmax, 2),
                                                  bolt_line=self.web_plate.bolt_line,
                                                  shear_load=round(self.fact_shear_load / 1000, 2),
                                                  axial_load=round(self.axial_force_w / 1000, 2),
                                                  moment_demand=round(self.web_plate.moment_demand / 1000000, 2),
                                                  r=round(self.web_plate.sigma_r_sq / 1000, 2),
                                                  vbv=round(self.web_plate.vbv / 1000, 2),
                                                  tmv=round(self.web_plate.tmv / 1000, 2),
                                                  tmh=round(self.web_plate.tmh / 1000, 2),
                                                  abh=round(self.web_plate.abh / 1000, 2),
                                                  vres=round(self.web_plate.bolt_force / 1000, 2)), '')
        self.report_check.append(t10)

        t10 = (KEY_OUT_LONG_JOINT, long_joint_bolted_req(),
               long_joint_bolted_prov(self.web_plate.bolt_line, self.web_plate.bolts_one_line,
                                      self.web_plate.pitch_provided,
                                      self.web_plate.gauge_provided, self.bolt.bolt_diameter_provided,
                                      web_bolt_capacity_kn,
                                      web_bolt_capacity_red_kn), "")
        self.report_check.append(t10)

        t5 = (KEY_OUT_DISP_BOLT_CAPACITY, round(self.web_plate.bolt_force / 1000, 2), web_bolt_capacity_red_kn,
              get_pass_fail(round(self.web_plate.bolt_force / 1000, 2), web_bolt_capacity_red_kn, relation="lesser"))
        self.report_check.append(t5)

        ######Flange plate check####
        if self.preference == "Outside":
            t1 = ('SubSection', 'Outer flange plate Checks', '|p{4cm}|p{6cm}|p{5.5cm}|p{1.5cm}|')
            self.report_check.append(t1)

            t1 = (DISP_MIN_PLATE_HEIGHT, min_flange_plate_ht_req(beam_width=self.section.flange_width,
                                                                 min_flange_plate_ht=self.min_plate_height),
                  self.flange_plate.height,
                  get_pass_fail(self.min_plate_height, self.flange_plate.height, relation="lesser"))
            self.report_check.append(t1)

            min_plate_length = 2 * (((self.flange_plate.bolt_line / 2 - 1) * self.flange_bolt.min_pitch) + (
                    2 * self.flange_bolt.min_end_dist) + (self.flange_plate.gap / 2))

            t1 = (DISP_MIN_PLATE_LENGTH, min_flange_plate_length_req(min_pitch=self.flange_bolt.min_pitch,
                                                                     min_end_dist=self.flange_bolt.min_end_dist,
                                                                     bolt_line=self.flange_plate.bolt_line,
                                                                     min_length=min_plate_length,
                                                                     gap=self.flange_plate.gap),
                  self.flange_plate.length,
                  get_pass_fail(min_plate_length, self.flange_plate.length, relation="lesser"))
            self.report_check.append(t1)
            t1 = (DISP_MIN_PLATE_THICK, min_plate_thk_req(self.section.flange_thickness),
                  self.flange_plate.thickness_provided,
                  get_pass_fail(self.section.flange_thickness, self.flange_plate.thickness_provided, relation="lesser"))
            self.report_check.append(t1)
        else:
            t1 = ('SubSection', 'Inner and Outer flange plate Checks', '|p{4cm}|p{6cm}|p{5.5cm}|p{1.5cm}|')
            self.report_check.append(t1)
            ####OUTER PLATE####
            t1 = (DISP_MIN_PLATE_HEIGHT, min_flange_plate_ht_req(beam_width=self.section.flange_width,
                                                                 min_flange_plate_ht=self.min_plate_height),
                  self.flange_plate.height,
                  get_pass_fail(self.min_plate_height, self.flange_plate.height, relation="lesser"))
            self.report_check.append(t1)

            min_plate_length = 2 * (((self.flange_plate.bolt_line / 2 - 1) * self.flange_bolt.min_pitch) + (
                    2 * self.flange_bolt.min_end_dist) + (self.flange_plate.gap / 2))

            t1 = (DISP_MIN_PLATE_LENGTH, min_flange_plate_length_req(min_pitch=self.flange_bolt.min_pitch,
                                                                     min_end_dist=self.flange_bolt.min_end_dist,
                                                                     bolt_line=self.flange_plate.bolt_line,
                                                                     min_length=min_plate_length,
                                                                     gap=self.flange_plate.gap),
                  self.flange_plate.length,
                  get_pass_fail(min_plate_length, self.flange_plate.length, relation="lesser"))
            self.report_check.append(t1)
            ######INNER PLATE
            t1 = (DISP_MIN_PLATE_INNERHEIGHT, min_inner_flange_plate_ht_req(beam_width=self.section.flange_width,
                                                                            web_thickness=self.section.web_thickness,
                                                                            root_radius=self.section.root_radius,
                                                                            min_inner_flange_plate_ht=self.flange_plate.Innerheight),
                  self.flange_plate.Innerheight,
                  get_pass_fail(self.flange_plate.Innerheight, self.flange_plate.Innerheight, relation="lesser"))
            self.report_check.append(t1)
            t1 = (DISP_MAX_PLATE_INNERHEIGHT, min_inner_flange_plate_ht_req(beam_width=self.section.flange_width,
                                                                            web_thickness=self.section.web_thickness,
                                                                            root_radius=self.section.root_radius,
                                                                            min_inner_flange_plate_ht=self.flange_plate.Innerheight),
                  self.flange_plate.Innerheight, get_pass_fail(self.flange_plate.Innerheight,
                                                               self.flange_plate.Innerheight,
                                                               relation="lesser"))
            self.report_check.append(t1)

            min_plate_length = 2 * (((self.flange_plate.bolt_line / 2 - 1) * self.flange_bolt.min_pitch) + (
                    2 * self.flange_bolt.min_end_dist) + (self.flange_plate.gap / 2))

            t1 = (DISP_MIN_PLATE_INNERLENGTH, min_flange_plate_length_req(min_pitch=self.flange_bolt.min_pitch,
                                                                          min_end_dist=self.flange_bolt.min_end_dist,
                                                                          bolt_line=self.flange_plate.bolt_line,
                                                                          min_length=min_plate_length,
                                                                          gap=self.flange_plate.gap),
                  self.flange_plate.length,
                  get_pass_fail(min_plate_length, self.flange_plate.length, relation="lesser"))
            self.report_check.append(t1)
            t1 = (DISP_MIN_PLATE_THICK, min_plate_thk_req(self.section.flange_thickness / 2),
                  self.flange_plate.thickness_provided,
                  get_pass_fail(self.section.flange_thickness / 2, self.flange_plate.thickness_provided,
                                relation="lesser"))
            self.report_check.append(t1)

        ###################
        # Member Capacities
        ###################
        ### Flange Check ###
        t1 = ('SubSection', 'Member Checks', '|p{4cm}|p{6cm}|p{5.5cm}|p{1.5cm}|')
        self.report_check.append(t1)
        gamma_m0 = IS800_2007.cl_5_4_1_Table_5["gamma_m0"]['yielding']

        t1 = (KEY_DISP_TENSIONYIELDINGCAP_FLANGE, '', tension_yield_prov(self.flange_plate.height,
                                                                         self.section.flange_thickness,
                                                                         self.section.fy, gamma_m0,
                                                                         round(
                                                                             self.section.tension_yielding_capacity / 1000,
                                                                             2)), '')
        self.report_check.append(t1)
        gamma_m1 = IS800_2007.cl_5_4_1_Table_5["gamma_m1"]['ultimate_stress']

        t1 = (KEY_DISP_TENSIONRUPTURECAP_FLANGE, '', tension_rupture_bolted_prov(w_p=self.flange_plate.height,
                                                                                 t_p=self.section.flange_thickness,
                                                                                 n_c=self.flange_plate.bolts_one_line,
                                                                                 d_o=self.flange_bolt.dia_hole,
                                                                                 fu=self.section.fu, gamma_m1=gamma_m1,
                                                                                 T_dn=round(
                                                                                     self.section.tension_rupture_capacity / 1000,
                                                                                     2)), '')

        self.report_check.append(t1)

        t6 = (
        KEY_DISP_BLOCKSHEARCAP_FLANGE, '', blockshear_prov(Tdb=round(self.section.block_shear_capacity / 1000, 2)), '')
        self.report_check.append(t6)

        t1 = (KEY_DISP_FLANGE_TEN_CAPACITY, display_prov(round(self.flange_force / 1000, 2), "f_f"),

              tensile_capacity_prov(round(self.section.tension_yielding_capacity / 1000, 2),
                                    round(self.section.tension_rupture_capacity / 1000, 2),
                                    round(self.section.block_shear_capacity / 1000, 2)),
              get_pass_fail(round(self.flange_force / 1000, 2), round(self.section.tension_capacity_flange / 1000, 2),
                            relation="lesser"))
        self.report_check.append(t1)

        ### web Check ###
        gamma_m0 = IS800_2007.cl_5_4_1_Table_5["gamma_m0"]['yielding']
        # A_v_web = (self.section.depth - 2 * self.section.flange_thickness) * self.section.web_thickness
        webheight = (self.section.depth - 2 * self.section.flange_thickness)
        t1 = (KEY_DISP_TENSIONYIELDINGCAP_WEB, '', tension_yield_prov(webheight,
                                                                      self.section.web_thickness,
                                                                      self.section.fy, gamma_m0,
                                                                      round(
                                                                          self.section.tension_yielding_capacity_web / 1000,
                                                                          2)), '')
        self.report_check.append(t1)
        gamma_m1 = IS800_2007.cl_5_4_1_Table_5["gamma_m1"]['ultimate_stress']

        t1 = (KEY_DISP_TENSIONRUPTURECAP_WEB, '', tension_rupture_bolted_prov(w_p=webheight,
                                                                              t_p=self.section.web_thickness,
                                                                              n_c=self.web_plate.bolts_one_line,
                                                                              d_o=self.web_bolt.dia_hole,
                                                                              fu=self.section.fu, gamma_m1=gamma_m1,
                                                                              T_dn=round(
                                                                                  self.section.tension_rupture_capacity_web / 1000,
                                                                                  2)), '')
        self.report_check.append(t1)

        t1 = (
        KEY_DISP_BLOCKSHEARCAP_WEB, '', blockshear_prov(Tdb=round(self.section.block_shear_capacity_web / 1000, 2)), '')

        self.report_check.append(t1)

        t1 = (KEY_DISP_WEB_TEN_CAPACITY, display_prov(round(self.axial_force_w / 1000, 2), "A_w"),

              tensile_capacity_prov(round(self.section.tension_yielding_capacity_web / 1000, 2),
                                    round(self.section.tension_rupture_capacity_web / 1000, 2),
                                    round(self.section.block_shear_capacity_web / 1000, 2)),
              get_pass_fail(round(self.axial_force_w / 1000, 2), round(self.section.tension_capacity_web / 1000, 2),
                            relation="lesser"))
        self.report_check.append(t1)
        ###################
        # Flange plate Capacities check
        ###################
        if self.preference == "Outside":

            t1 = ('SubSection', 'Flange Plate Capacity Checks in Axial-Outside ', '|p{4cm}|p{6cm}|p{5.5cm}|p{1.5cm}|')
            self.report_check.append(t1)
            gamma_m0 = IS800_2007.cl_5_4_1_Table_5["gamma_m0"]['yielding']

            t1 = (KEY_DISP_TENSION_YIELDCAPACITY, '', tension_yield_prov(self.flange_plate.height,
                                                                         self.flange_plate.thickness_provided,
                                                                         self.flange_plate.fy, gamma_m0,
                                                                         round(
                                                                             self.flange_plate.tension_yielding_capacity / 1000,
                                                                             2)), '')
            self.report_check.append(t1)
            gamma_m1 = IS800_2007.cl_5_4_1_Table_5["gamma_m1"]['ultimate_stress']

            t1 = (KEY_DISP_TENSION_RUPTURECAPACITY, '', tension_rupture_bolted_prov(w_p=self.flange_plate.height,
                                                                                    t_p=self.flange_plate.thickness_provided,
                                                                                    n_c=self.flange_plate.bolts_one_line,
                                                                                    d_o=self.flange_bolt.dia_hole,
                                                                                    fu=self.flange_plate.fu,
                                                                                    gamma_m1=gamma_m1,
                                                                                    T_dn=round(
                                                                                        self.flange_plate.tension_rupture_capacity / 1000,
                                                                                        2)), '')
            self.report_check.append(t1)

            t1 = (KEY_DISP_TENSION_BLOCKSHEARCAPACITY, '',
                  blockshear_prov(Tdb=round(self.flange_plate.block_shear_capacity / 1000, 2)), '')

            self.report_check.append(t1)

            t1 = (KEY_DISP_FLANGE_PLATE_TEN_CAP, display_prov(round(self.flange_force / 1000, 2), "f_f"),
                  tensile_capacity_prov(round(self.flange_plate.tension_yielding_capacity / 1000, 2),
                                        round(self.flange_plate.tension_rupture_capacity / 1000, 2),
                                        round(self.flange_plate.block_shear_capacity / 1000, 2)),
                  get_pass_fail(round(self.flange_force / 1000, 2),
                                round(self.flange_plate.tension_capacity_flange_plate / 1000, 2),
                                relation="lesser"))
            self.report_check.append(t1)
        else:
            t1 = (
            'SubSection', 'Flange Plate Capacity Checks in axial-Outside/Inside ', '|p{4cm}|p{6cm}|p{5.5cm}|p{1.5cm}|')
            self.report_check.append(t1)
            gamma_m0 = IS800_2007.cl_5_4_1_Table_5["gamma_m0"]['yielding']
            total_height = self.flange_plate.height + (2 * self.flange_plate.Innerheight)

            t1 = (KEY_DISP_TENSION_YIELDCAPACITY, '', tension_yield_prov(total_height,
                                                                         self.flange_plate.thickness_provided,
                                                                         self.flange_plate.fy, gamma_m0,
                                                                         round(
                                                                             self.flange_plate.tension_yielding_capacity / 1000,
                                                                             2)), '')
            self.report_check.append(t1)

            gamma_m1 = IS800_2007.cl_5_4_1_Table_5["gamma_m1"]['ultimate_stress']

            t1 = (KEY_DISP_TENSION_RUPTURECAPACITY, '', tension_rupture_bolted_prov(w_p=total_height,
                                                                                    t_p=self.flange_plate.thickness_provided,
                                                                                    n_c=self.flange_plate.bolts_one_line,
                                                                                    d_o=self.flange_bolt.dia_hole,
                                                                                    fu=self.flange_plate.fu,
                                                                                    gamma_m1=gamma_m1,
                                                                                    T_dn=round(
                                                                                        self.flange_plate.tension_rupture_capacity / 1000,
                                                                                        2)), '')
            self.report_check.append(t1)

            t1 = (KEY_DISP_TENSION_BLOCKSHEARCAPACITY, '',
                  blockshear_prov(Tdb=round(self.flange_plate.block_shear_capacity / 1000, 2)), '')

            self.report_check.append(t1)

            t1 = (KEY_DISP_FLANGE_PLATE_TEN_CAP, display_prov(round(self.flange_force / 1000, 2), "f_f"),
                  tensile_capacity_prov(round(self.flange_plate.tension_yielding_capacity / 1000, 2),
                                        round(self.flange_plate.tension_rupture_capacity / 1000, 2),
                                        round(self.flange_plate.block_shear_capacity / 1000, 2)),
                  get_pass_fail(round(self.flange_force / 1000, 2),
                                round(self.flange_plate.tension_capacity_flange_plate / 1000, 2),
                                relation="lesser"))
            self.report_check.append(t1)

        ###################
        # Web plate Capacities check axial
        ###################
        t1 = ('SubSection', 'Web Plate Capacity Checks in Axial', '|p{4cm}|p{6cm}|p{5.5cm}|p{1.5cm}|')
        self.report_check.append(t1)
        gamma_m0 = IS800_2007.cl_5_4_1_Table_5["gamma_m0"]['yielding']

        t1 = (KEY_DISP_TENSION_YIELDCAPACITY, '', tension_yield_prov(self.web_plate.height,
                                                                     self.web_plate.thickness_provided,
                                                                     self.web_plate.fy,
                                                                     gamma_m0,
                                                                     round(
                                                                         self.web_plate.shear_yielding_capacity / 1000,
                                                                         2)), '')

        self.report_check.append(t1)
        gamma_m1 = IS800_2007.cl_5_4_1_Table_5["gamma_m1"]['ultimate_stress']

        t1 = (KEY_DISP_TENSION_RUPTURECAPACITY, '', tension_rupture_bolted_prov(self.web_plate.height,
                                                                                self.web_plate.thickness_provided,
                                                                                self.web_plate.bolts_one_line,
                                                                                self.web_bolt.dia_hole,
                                                                                self.web_bolt.fu, gamma_m1,
                                                                                round(
                                                                                    self.web_plate.tension_rupture_capacity / 1000,
                                                                                    2)), '')

        self.report_check.append(t1)

        t1 = (KEY_DISP_TENSION_BLOCKSHEARCAPACITY, '',
              blockshear_prov(Tdb=round(self.web_plate.block_shear_capacity / 1000, 2)), '')
        self.report_check.append(t1)

        t1 = (KEY_DISP_TEN_CAP_WEB_PLATE, display_prov(round(self.axial_force_w / 1000, 2), "A_w"),
              tensile_capacity_prov(round(self.web_plate.tension_yielding_capacity / 1000, 2),
                                    round(self.web_plate.tension_rupture_capacity / 1000, 2),
                                    round(self.web_plate.block_shear_capacity / 1000, 2)),
              get_pass_fail(round(self.axial_force_w / 1000, 2),
                            round(self.web_plate.tension_capacity_web_plate / 1000, 2),
                            relation="lesser"))
        self.report_check.append(t1)

        ###################
        # Web plate Capacities check Shear
        ###################
        t1 = ('SubSection', 'Web Plate Capacity Checks in Shear', '|p{4cm}|p{6cm}|p{5.5cm}|p{1.5cm}|')
        self.report_check.append(t1)

        t1 = (KEY_DISP_SHEAR_YLD, '', shear_yield_prov(self.web_plate.height, self.web_plate.thickness_provided,
                                                       self.web_plate.fy, gamma_m0,
                                                       round(self.web_plate.shear_yielding_capacity / 1000, 2)), '')
        self.report_check.append(t1)

        t1 = (KEY_DISP_SHEAR_RUP, '', shear_rupture_prov_beam(self.web_plate.height, self.web_plate.thickness_provided,
                                                              self.web_plate.bolt_line / 2, self.web_bolt.dia_hole,
                                                              self.web_plate.fu,

                                                              round(self.web_plate.shear_rupture_capacity / 1000, 2),
                                                              gamma_m1), '')

        self.report_check.append(t1)

        t1 = (KEY_DISP_PLATE_BLK_SHEAR_SHEAR, '',
              blockshear_prov(Tdb=round(self.web_plate.block_shear_capacity_shear / 1000, 2)), '')
        self.report_check.append(t1)

        t1 = (KEY_DISP_WEBPLATE_SHEAR_CAPACITY, display_prov(round(self.fact_shear_load / 1000, 2), "V_u"),

              shear_capacity_prov(round(self.web_plate.shear_yielding_capacity / 1000, 2),
                                  round(self.web_plate.shear_rupture_capacity / 1000, 2),
                                  round(self.web_plate.block_shear_capacity / 1000, 2)),
              get_pass_fail(round(self.fact_shear_load / 1000, 2),
                            round(self.web_plate.shear_capacity_web_plate / 1000, 2), relation="lesser"))
        self.report_check.append(t1)

        Disp_3D_image = "/ResourceFiles/images/3d.png"

        #config = configparser.ConfigParser()
        #config.read_file(open(r'Osdag.config'))
        #desktop_path = config.get("desktop_path", "path1")
        #print("desk:", desktop_path)
        print(sys.path[0])
        rel_path = str(sys.path[0])
        rel_path = rel_path.replace("\\", "/")

        fname_no_ext = popup_summary['filename']


        CreateLatex.save_latex(CreateLatex(), self.report_input, self.report_check, popup_summary, fname_no_ext,
                               rel_path, Disp_3D_image)

# def save_latex(self, uiObj, Design_Check, reportsummary, filename, rel_path, Disp_3d_image):
