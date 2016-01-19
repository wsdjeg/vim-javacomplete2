import deoplete.util

from .base import Base

class Source(Base):
    def __init__(self, vim):
        Base.__init__(self, vim)

        self.name = 'java'
        self.mark = ''
        self.filetypes = ['java']
        self.min_pattern_length = 0
        self.is_bytepos = True

    def get_complete_api(self, findstart):
        return self.vim.call('javacomplete#Complete', findstart, 0)

    def get_complete_position(self, context):
        return self.get_complete_api(1)

    def gather_candidates(self, context):
        return self.get_complete_api(0)
