from __future__ import absolute_import, unicode_literals

from markdown import Extension
from markdown.treeprocessors import Treeprocessor


class AutoDirectionTreeprocessor(Treeprocessor):
    def run(self, root):
        blocks = root.iter('p')
        for block in blocks:
            block.set('dir', 'auto')


class AutoDirectionExtension(Extension):
    def extendMarkdown(self, md):
        autodirection = AutoDirectionTreeprocessor(md)
        md.treeprocessors.register(autodirection, 'autodirection', 50)
        md.registerExtension(self)


def makeExtension(**kwargs):  # pragma: no cover
    return AutoDirectionExtension(**kwargs)
