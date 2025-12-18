import datetime
import pandas as pd

class Incident:
    """Class to represent a Cybersecurity Incident (Week 11 Requirement)"""

    def __init__(self, incident_id, title, category, severity, status, date_reported, date_resolved=None):
        self.id = incident_id
        self.title = title
        self.category = category
        self.severity = severity
        self.status = status
        self.date_reported = date_reported
        self.date_resolved = date_resolved

    def calculate_resolution_time(self):
        """Calculates hours taken to resolve the incident"""
        if self.date_resolved and self.date_reported:
            # Convert strings to datetime if necessary
            start = pd.to_datetime(self.date_reported)
            end = pd.to_datetime(self.date_resolved)
            duration = end - start
            return duration.total_seconds() / 3600
        return None

    def get_summary(self):
        """Returns a formatted string for the AI Assistant to use"""
        return f"Incident {self.id}: {self.title} ({self.category}) - Status: {self.status}"
