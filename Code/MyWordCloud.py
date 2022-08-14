import pandas as pd
import numpy as np
from wordcloud import WordCloud, STOPWORDS
# converting string representation of list to list:ast.literal_eval "['abc','de']"->['abc','de']
import ast
import matplotlib.pyplot as plt


def rand_color_func(word, font_size, position, orientation, random_state=None,
                    **kwargs):
    """
    this function is used to change color of wordcloud;now is orange color
    :return: a string of hsl color(Hue, Saturation, Luminosity)
    """
    h = int(360.0 * 21.0 / 255.0)
    s = int(100.0 * 255.0 / 255.0)
    l = int(100.0 * float(random_state.randint(60, 120)) / 255.0)
    return "hsl({}, {}%, {}%)".format(h, s, l)


class draw_wordcloud:
    def __init__(self, path):
        """
        :param path: path to data file
        """
        self.path = path
        self.top_brands = list()
        self.low_brands = list()
        self.brands = list()

    def load_data(self):
        """this function is used to clean df
        given data file path
        """
        self.df = pd.read_csv(self.path)
        if "result" in self.df.columns:
            self.df["result"] = self.df["result"].apply(
                lambda s: ast.literal_eval(s))  # string of list->list
        else:
            print("Something wrong with columns")

    def load_brands(self):
        """this function is used to load brands exisiting in dataset
        and categorize into low/top/specific brands
        """
        if "brand" not in self.df.columns:
            print("Something wrong with columns")
        else:
            if self.path.find("bot") >= 0:  # if found
                self.low_brands = self.df.brand.unique().tolist()
                self.brands += self.low_brands
            elif self.path.find("top") >= 0:
                self.top_brands = self.df.brand.unique().tolist()
                self.brands += self.top_brands

            elif self.path.find("specific") >= 0:
                self.brands += self.df.brand.unique().tolist()

    def separate_df(self, no_brand=True):
        """this function is used to separate out dataframe for each brand
        :param no_brand:whether to drop "brand" column
        :return: dict {brand_name:df/Series}
        """
        result = dict()
        for b in self.brands:
            b_df = self.df.loc[self.df.brand == b, :]
            if no_brand:
                b_df.drop("brand", axis=1, inplace=True)
            result[b] = b_df
        return result

    def processing_text(self, brand_dict):
        """this function is used to combine lists of tokenized words into a big string
        eg: [skeptical, vacuum, feature, actually, work..]->"skeptical vacuum.."
        :param brand_dict: dict {brand_name:df/Series}
        return: dict {brand_name:string including all reviews}
        """
        result = dict()
        for b in brand_dict:
            # df(1/2 coln) with each element a list of words
            s = brand_dict[b]

            # series with each element a string
            review_s = s["result"].apply(lambda l: " ".join(l))
            whole_text = ""
            for rev in review_s:
                whole_text += rev
                whole_text += " "
            result[b] = whole_text
        return result

    def plot(self, brand, bstring_dict, extra=None):
        """this function is used to plot wordclouds for each brand
        requires one big string,then remove stopwords(default + customized)->wordcloud
        :param brand: one brand name to draw wordcloud for
        :param bstring_dict: dict {brand_name:one string combining all keywords}
        :param extra: list of extra stopwords given by user
        :return:wordcloud graph
        """
        stops = set(
            STOPWORDS)  # dict->set #everytime call "plot":RE-intialize stops!
        if extra:
            stops.update(extra)  # or:add(word)
        # text_dict = self.processing_text()
        # whole_text = text_dict[brand]

        whole_text = bstring_dict[brand]
        wordcloud = WordCloud(width=800, height=800,
                              background_color='white',
                              collocations=False,  # not include bigram
                              stopwords=stops,
                              min_font_size=10).generate(whole_text)

        # plt.figure(figsize=(10, 10), facecolor=None)
        # plt.title(f"Keywords for {brand}", fontsize=20)
        # plt.imshow(wordcloud, interpolation="bilinear")
        # plt.axis("off")
        # wordcloud.to_file(f"./images/{brand}_wc.png")
        # print(brand, "is saved")
        # plt.show()

        default_colors = wordcloud.to_array()
        if brand in self.low_brands:  # low brand
            plt.figure(figsize=(10, 10), facecolor=None)
            plt.title(f"Bottom brands:{brand}", fontsize=20)
            plt.imshow(wordcloud.recolor(color_func=rand_color_func, random_state=42),
                       interpolation="bilinear")
            plt.axis("off")
            wordcloud.to_file(f"./images/{brand}_wc.png")
            print(brand, "is saved")
            plt.show()
        else:  # top brands + specific brands
            plt.figure(figsize=(10, 10), facecolor=None)
            plt.title(f"Top brands:{brand}", fontsize=20)
            plt.imshow(default_colors, interpolation="bilinear")
            plt.axis("off")
            wordcloud.to_file(f"./images/{brand}_wc.png")
            print(brand, "is saved")
            plt.show()

    def main(self, no_brand=True, stopw=None):
        """main function of the class
        only need to run this method when import the class
        :param no_brand: bool,whether to drop "brand" column when sep out df for each brand
        :param stopw: list,customized stopwords provided by user
        """
        self.load_data()
        self.load_brands()
        brands_d = self.separate_df(no_brand=no_brand)
        brands_string = self.processing_text(brand_dict=brands_d)
        for brand in self.brands:
            self.plot(brand, brands_string, extra=stopw)


# def random_color_func(word=None, font_size=None, position=None,
#                       orientation=None, font_path=None, random_state=None):
#     """Random hue color generation.

#     Default coloring method. This just picks a random hue with value 80% and
#     lumination 50%.

#     Parameters
#     ----------
#     word, font_size, position, orientation  : ignored.

#     random_state : random.Random object or None, (default=None)
#         If a random object is given, this is used for generating random
#         numbers.

#     """
#     if random_state is None:
#         random_state = Random()
#     return "hsl(%d, 80%%, 50%%)" % random_state.randint(0, 255)


# def recolor(self, random_state=None, color_func=None, colormap=None):
#     """Recolor existing layout.

#     Applying a new coloring is much faster than generating the whole
#     wordcloud.

#     Parameters
#     ----------
#     random_state : RandomState, int, or None, default=None
#         If not None, a fixed random state is used. If an int is given, this
#         is used as seed for a random.Random state.

#     color_func : function or None, default=None
#         Function to generate new color from word count, font size, position
#         and orientation.  If None, self.color_func is used.

#     colormap : string or matplotlib colormap, default=None
#         Use this colormap to generate new colors. Ignored if color_func
#         is specified. If None, self.color_func (or self.color_map) is used.

#     Returns
#     -------
#     self
#     """
#     if isinstance(random_state, int):
#         random_state = Random(random_state)
#     self._check_generated()

#     if color_func is None:
#         if colormap is None:
#             color_func = self.color_func
#         else:
#             color_func = colormap_color_func(colormap)
#     self.layout_ = [(word_freq, font_size, position, orientation,
#                      color_func(word=word_freq[0], font_size=font_size,
#                                 position=position, orientation=orientation,
#                                 random_state=random_state,
#                                 font_path=self.font_path))
#                     for word_freq, font_size, position, orientation, _
#                     in self.layout_]
#     return self
