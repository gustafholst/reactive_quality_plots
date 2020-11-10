import pandas as pd
import matplotlib.pyplot as plt

colors = {'original': '#cedece', 'reactive': '#0a5e0c'}
header_printed = False


def read_holst_datasets():
    global holst_orig
    global holst_rx
    holst_orig = pd.read_csv("D:\OpenSourceProjects\ReadabilityFeaturesCalculator\DATASET_HOLST_ORIGINAL.csv", sep=';')
    holst_rx = pd.read_csv("D:\OpenSourceProjects\ReadabilityFeaturesCalculator\DATASET_HOLST_REACTIVE.csv", sep=';')

    global num_rows
    num_rows = len(holst_orig.index)


def draw_plot(params):
    # Group by index labels and take the means and standard deviations
    # for each group
    df = params['df']
    title = params['title']
    ylabel = params['ylabel']
    filename = params['filename']

    gp = df.groupby(by=['feature']).mean()

    errors = df.groupby(by=['feature']).std()

    # Plot
    fig, ax = plt.subplots()

    gp.plot.bar(yerr=errors, ax=ax, capsize=4, rot=0, color=colors)
    #gp.plot.box(yerr=errors, ax=ax)

    plt.title(title)
    plt.ylabel(ylabel)
    plt.xlabel("")
    plt.grid(b=True, which='major', axis='y')

    if save_plots:
        plt.savefig(filename)
    else:
        plt.show()


def draw_line_length_plot():
    original_max_line_length = holst_orig['BW Max line length']
    rx_max_line_length = holst_rx['BW Max line length']

    original_avg_line_length = holst_orig['BW Avg line length']
    rx_avg_line_length = holst_rx['BW Avg line length']

    max_list = ['max'] * original_max_line_length.size
    avg_list = ['avg'] * original_avg_line_length.size

    df = pd.DataFrame({
        'feature': [*max_list, *avg_list],
        'original': [*original_max_line_length.values.flatten(), *original_avg_line_length.values.flatten()],
        'reactive': [*rx_max_line_length.values.flatten(), *rx_avg_line_length.values.flatten()],
    })

    params = {
        'df': df,
        'title': "Line length",
        'ylabel': "length",
        'filename': "line_length"
    }

    draw_plot(params)

    display_table_header()
    display_table_row("max line length", original_max_line_length, rx_max_line_length)
    display_table_row("avg line length", original_avg_line_length, rx_avg_line_length)


def draw_stops_parens_ident_plot():
    original_avg_parenthesis = holst_orig['BW Avg parenthesis']
    rx_avg_parenthesis = holst_rx['BW Avg parenthesis']
    original_avg_identifiers = holst_orig['BW Avg number of identifiers']
    rx_avg_identifiers = holst_rx['BW Avg number of identifiers']
    original_avg_periods = holst_orig['BW Avg periods']
    rx_avg_periods = holst_rx['BW Avg periods']

    parens = ['#() {}'] * original_avg_parenthesis.size
    stops = ['#.'] * original_avg_parenthesis.size
    ident = ['#ident'] * original_avg_parenthesis.size

    df = pd.DataFrame({
        'feature': [*parens, *stops, *ident],
        'original': [*original_avg_parenthesis.values, *original_avg_periods.values, *original_avg_identifiers.values],
        'reactive': [*rx_avg_parenthesis.values, *rx_avg_periods.values, *rx_avg_identifiers.values]
    })

    params = {
        'df': df,
        'title': "Average number of features per line",
        'ylabel': "number of ocurrences",
        'filename': "avg_features"
    }

    draw_plot(params)

    display_table_header()
    display_table_row("avg_parenthesis", original_avg_parenthesis, rx_avg_parenthesis)
    display_table_row("avg_identifiers", original_avg_identifiers, rx_avg_identifiers)
    display_table_row("avg_periods", original_avg_periods, rx_avg_periods)


def draw_cyc_plot():
    cyc_orig = holst_orig['cyclomatic_complexity']
    cyc_rx = holst_rx['cyclomatic_complexity']

    cyc = ['CYC'] * num_rows

    df = pd.DataFrame({
        'feature': cyc,
        'original': cyc_orig,
        'reactive': cyc_rx
    })

    params = {
        'df': df,
        'title': "Cyclomatic Complexity",
        'ylabel': "complexity",
        'filename': "cyc"
    }

    draw_plot(params)

    display_table_header()
    display_table_row("CYC", cyc_orig, cyc_rx)


def draw_readabilities_plot():
    buse_orig = holst_orig['buse_readability']
    buse_rx = holst_rx['buse_readability']
    scalabrino_orig = holst_orig['scalabrino_readability']
    scalabrino_rx = holst_rx['scalabrino_readability']

    BW = ['B&W'] * num_rows
    SC = ['SC'] * num_rows

    df = pd.DataFrame({
        'feature': [*BW, *SC],
        'original': [*buse_orig, *scalabrino_orig],
        'reactive': [*buse_rx, *scalabrino_rx]
    })

    params = {
        'df': df,
        'title': "Readability",
        'ylabel': "readability",
        'filename': "readabilities"
    }

    draw_plot(params)

    display_table_header()
    display_table_row("B&W", buse_orig, buse_rx)
    display_table_row("SC", scalabrino_orig, scalabrino_rx)


def draw_cyc_features_plot():
    num_and_or_orig = holst_orig['num_and_or']
    num_and_or_rx = holst_rx['num_and_or']
    num_catch_orig = holst_orig['num_catch']
    num_catch_rx = holst_rx['num_catch']
    num_if_statements_orig = holst_orig['num_if_statements']
    num_if_statements_rx = holst_rx['num_if_statements']
    num_loops_orig = holst_orig['num_loops']
    num_loops_rx = holst_rx['num_loops']
    num_throws_orig = holst_orig['num_throws']
    num_throws_rx = holst_rx['num_throws']

    catch = ['#catch'] * num_rows
    and_or = ['#&&, ||'] * num_rows
    loops = ['#loops'] * num_rows
    if_stmts = ['#if'] * num_rows
    throw_stmt = ['#throw'] * num_rows

    df = pd.DataFrame({
        'feature': [*loops, *if_stmts, *catch, *and_or, *throw_stmt],
        'original': [*num_loops_orig, *num_if_statements_orig, *num_catch_orig, *num_and_or_orig, *num_throws_orig],
        'reactive': [*num_loops_rx, *num_if_statements_rx, *num_catch_rx, *num_and_or_rx, *num_throws_rx]
    })

    params = {
        'df': df,
        'title': "CYC features",
        'ylabel': "number of statements per method",
        'filename': "cyc_features"
    }

    draw_plot(params)


def draw_loc_plot():
    loc_orig = holst_orig['lines_of_code']
    loc_rx = holst_rx['lines_of_code']

    loc = ['LOC'] * num_rows

    df = pd.DataFrame({
        'feature': loc,
        'original': loc_orig,
        'reactive': loc_rx
    })

    params = {
        'df': df,
        'title': "Lines of code",
        'ylabel': "number of lines",
        'filename': "loc"
    }

    draw_plot(params)

    display_table_header()
    display_table_row("LOC", loc_orig, loc_rx)

    print("total LOC original: ", loc_orig.sum())
    print("total LOC refactored: ", loc_rx.sum())


def calculate_diff(val1, val2):
    return ((val1 - val2) / val1) * -1


def print_value(name, value):
    print(name, round(value, 2))


def display_table_header():
    global header_printed

    if not header_printed:
        print("{:^16}\t{:<14}\t{:<14}\t{}".format("measure", "OO mean/std", "RP mean/std", "diff (%)"))
        print("{:^16}\t{:<14}\t{:<14}\t{}".format("-------", "-----------", "-----------", "--------"))
        header_printed = True


def display_table_row(name, orig_df, refactored_df):
    orig_mean = orig_df.mean()
    refactored_mean = refactored_df.mean()
    orig_std = orig_df.std()
    refactored_std = refactored_df.std()
    diff = calculate_diff(orig_mean, refactored_mean)

    print("{:<16}\t{:.2f}+-{:<7.2f}\t{:.2f}+-{:<7.2f}\t{:.2%}"
          .format(name, orig_mean, orig_std, refactored_mean, refactored_std, diff))


def draw_most_readable():
    #for viewing pandas in terminal
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', 200)

    new_column_name = 'change(%)'

    #merge the two datasets
    sc = pd.merge(holst_orig, holst_rx, how='inner', left_index=True, right_index=True, suffixes=('', '_rx'))

    #add a new column with change in percentage
    sc[new_column_name] = sc.apply(
        lambda row: calculate_diff(row.scalabrino_readability, row.scalabrino_readability_rx) * 100, axis=1)

    sc = sc[['class_name', 'signature', 'scalabrino_readability', 'scalabrino_readability_rx', new_column_name]]
    sc.sort_values(by=new_column_name, inplace=True)

    print(sc)


def main():
    read_holst_datasets()
    global save_plots
    save_plots = False

    # draw_cyc_plot()
    draw_loc_plot()
    # draw_readabilities_plot()
    # draw_cyc_features_plot()
    # draw_line_length_plot()
    # draw_stops_parens_ident_plot()
    # draw_most_readable()


if __name__ == "__main__":
    main()









# def draw_avg_identifiers_plot():
#     original_avg_identifiers = holst_orig['BW Avg number of identifiers']
#     rx_avg_identifiers = holst_rx['BW Avg number of identifiers']
#
#     avg = ['avg identifiers'] * original_avg_identifiers.size
#
#     df = pd.DataFrame({
#         'feature': avg,
#         'original': original_avg_identifiers.values,
#         'reactive': rx_avg_identifiers.values,
#     })
#
#     params = {
#         'df': df,
#         'title': "Average number of identifiers per line",
#         'ylabel': "number of ocurrences",
#         'filename': "avg_identifiers"
#     }
#
#     draw_plot(params)
#
# def draw_avg_periods_plot():
#     original_avg_periods = holst_orig['BW Avg periods']
#     rx_avg_periods = holst_rx['BW Avg periods']
#
#     avg = ['avg periods'] * original_avg_periods.size
#
#     df = pd.DataFrame({
#         'feature': avg,
#         'original': original_avg_periods.values,
#         'reactive': rx_avg_periods.values,
#     })
#
#     params = {
#         'df': df,
#         'title': "Average number of periods per line",
#         'ylabel': "number of ocurrences",
#         'filename': "avg_periods"
#     }
#
#     draw_plot(params)
#
#
# def draw_avg_parenthesis_plot():
#     original_avg_parenthesis = holst_orig['BW Avg parenthesis']
#     rx_avg_parenthesis = holst_rx['BW Avg parenthesis']
#
#     avg = ['avg parentheses and brackets'] * original_avg_parenthesis.size
#
#     df = pd.DataFrame({
#         'feature': avg,
#         'original': original_avg_parenthesis.values,
#         'reactive': rx_avg_parenthesis.values,
#     })
#
#     params = {
#         'df': df,
#         'title': "Average number of parenthesis and brackets per line",
#         'ylabel': "number of ocurrences",
#         'filename': "avg_parentheses"
#     }
#
#     draw_plot(params)
