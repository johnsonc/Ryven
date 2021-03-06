from NIENV import *


# API METHODS --------------

# self.main_widget
# self.update_shape()

# Ports
# self.input(index)
# self.set_output_val(index, val)
# self.exec_output(index)

# self.create_new_input(type_, label, widget_name=None, widget_pos='under', pos=-1)
# self.delete_input(index)
# self.create_new_output(type_, label, pos=-1)
# self.delete_output(index)

# Logging
# mylog = self.new_log('Example Log')
# mylog.log('I\'m alive!!')
# self.log_message('hello global!', target='global')
# self.log_message('that\'s not good', target='error')

# --------------------------
from sklearn.ensemble import RandomForestClassifier


class RFCSetParams_NodeInstance(NodeInstance):
    def __init__(self, params):
        super(RFCSetParams_NodeInstance, self).__init__(params)
        tmp = RandomForestClassifier()
        params = tmp.get_params()
        for key in params:
            self.create_new_input(type_="data", label=key, widget_name="std line edit m", widget_pos="besides", pos=-1)
        del tmp

    def update_event(self, input_called=-1):
        params = RandomForestClassifier().get_params()
        i = 0
        for key in params:
            if self.input(i) != "":
                params[key] = self.input(i)
            i += 1
    
        self.set_output_val(0, params)

    def get_data(self):
        data = {}
        return data

    def set_data(self, data):
        pass

    def removing(self):
        pass
