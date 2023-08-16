import androidDeveloper
import webDeveloper
class EmployeeFactory:
    @staticmethod
    def create_object(property):
        if property == 'androidDeveloper':
            return androidDeveloper.AndroidDeveloper()
        else:
            return webDeveloper.WebDeveloper()