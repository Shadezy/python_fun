def read_data(fileName):

    # Read the file, splitting by lines
    f = open(fileName, 'r');
    lines = f.read().splitlines();
    f.close();

    items = [];

    for i in range(1, len(lines)):
        line = lines[i].split(',');
        itemFeatures = [];

        for j in range(len(line)-1):
            v = float(line[j]); # Convert feature value to float
            itemFeatures.append(v); # Add feature value to dict

        items.append(itemFeatures);

    shuffle(items);

    return items;

def FindColMinMax(items):
    n = len(items[0]);
    minima = [sys.maxint for i in range(n)];
    maxima = [-sys.maxint -1 for i in range(n)];

    for item in items:
        for f in range(len(item)):
            if (item[f] < minima[f]):
                minima[f] = item[f];

            if (item[f] > maxima[f]):
                maxima[f] = item[f];

    return minima,maxima; 
