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
import numpy as np

class %CLASS%(NodeInstance):
    def __init__(self, params):
        super(%CLASS%, self).__init__(params)
        self.defpar = {"groups":None, "scoring":None, "cv":None, "n_jobs":None, "verbose":0, "fit_params":None, "pre_dispatch":'2*n_jobs', "error_score":np.nan}
        
        for key in self.defpar:
            self.create_new_input(type_="data", label=key, widget_name="std line edit m", widget_pos='besides', pos=-1)
        # self.special_actions['action name'] = {'method': M(self.action_method)}
        # ...

    def update_event(self, input_called=-1):
        params = {}
        for i in range(len(self.inputs)):
            if self.input(i) != "":
                params[self.inputs[i].label_str] = self.input(i)

        self.set_output_val(0, params)

    def get_data(self):
        data = {}
        return data

    def set_data(self, data):
        pass

    def removing(self):
        pass
