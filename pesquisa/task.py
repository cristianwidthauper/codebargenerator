import barcode
import os
import glob
from barcode.writer import ImageWriter
from PIL import Image


class Barcode_generator():
    def generate_barcodes(self):
        linhas = ['CTR', 'SUL', 'DSL']
        estacoes = {
            'CTR': ['REC', 'JOA', 'AFO', 'IPI', 'MAG', 'LUZ', 'WEK', 'BAR', 'TEJ', 'COQ', 'CEU', 'CDO', 'ROD', 'COS', 'GIB', 'CAV', 'FLO', 'ENG', 'JAB'],
            'SUL': ['PAZ', 'IMB', 'FAL', 'SHO', 'NEV', 'PTO', 'LAR', 'GUA', 'PRZ', 'CAJ'],
            'DSL': ['CUR', 'JOR', 'MAR', 'ANG', 'PTZ', 'PTC', 'SAN', 'CAB']
        }
        tipos = ['RUA', 'SEI', 'GRA']
        horarios = ['0506', '0607', '0708', '0809', '0910', '1011', '1112', '1213',
                    '1314', '1415', '1516', '1617', '1718', '1819', '1920', '2021', '2122', '2223']

        CODE = barcode.get_barcode_class('code39')

        for ct in estacoes['DSL']:
            for tip in tipos:
                for hor in horarios:
                    text = f'DSL.{ct}.{tip}.{hor}'
                    code = CODE(f'{text}.', writer=ImageWriter())
                    code.save(f'{text}', {
                        "module_width": 0.10,
                        "module_height": 6,
                        "text_distance": 1,
                        "font_size": 7})

    def merge_images(self):
        py_files = glob.glob(
            '/home/cristianwidthauper/Documentos/CBTU/' + '*.png')

        for x in py_files:
            im1 = Image.open('cartao.jpeg')
            im2 = Image.open(x)

            back_im = im1.copy()
            back_im.paste(im2, (30, 90))
            back_im.save(x.split('/')[5], quality=100)


a = Barcode_generator()
a.generate_barcodes()
a.merge_images()
