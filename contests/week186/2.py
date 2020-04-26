from typing import List


class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        if k==len(cardPoints): return sum(cardPoints)
        k = len(cardPoints)-k

        span_sum = sum(cardPoints[:k])
        min_value = span_sum

        for i in range(k, len(cardPoints)):
            span_sum  = span_sum-cardPoints[i-k]+cardPoints[i]
            if min_value>span_sum:
                min_value = span_sum

        return sum(cardPoints) - min_value

if __name__ == '__main__':
    s = Solution()
    cardPoints = [1, 79, 80, 1, 1, 1, 200, 1]
    k = 3

    ans = s.maxScore(cardPoints, k)
    print(ans)

    cardPoints = [1, 1000, 1]
    k = 1
    ans = s.maxScore(cardPoints, k)
    print(ans)

    cardPoints = [1, 2, 3, 4, 5, 6, 1]
    k = 3
    ans = s.maxScore(cardPoints, k)

    print(ans)

    # 232
    ans = s.maxScore([11, 49, 100, 20, 86, 29, 72], 4)

    print(ans)

    ans = s.maxScore([1, 2, 3, 4, 5, 6, 1], 3)
    print(ans)

    cards = [893,830,598,63,715,606,512,978,752,312,221,184,122,943,670,611,974,259,809,163,886,793,254,18,143,294,407,315,226,818,504,851,414,514,694,67,88,98,58,55,650,29,199,495,276,924,664,135,780,118,660,600,789,967,597,223,184,172,423,987,237,849,469,607,996,807,211,821,760,986,453,451,874,320,632,851,110,935,182,897,649,574,725,148,843,229,39,79,775,911,695,335,227,934,814,2,430,546,632,529,886,771,884,317,155,226,429,902,575,437,844,177,246,771,646,781,721,955,447,706,215,432,194,332,389,584,479,655,219,448,911,296,162,900,409,320,518,791,53,232,522,126,142,533,362,428,554,922,177,14,740,160,572,339,15,392,526,423,896,964,541,321,228,946,583,12,887,230,832,669,158,985,663,192,305,152,226,869,204,847,126,748,475,982,333,827,653,834,202,698,181,313,30,135,309,63,731,367,270,442,614,795,939,314,993,897,109,151,306,992,338,155,345,381,201,33,929,469,227,525,920,499,850,726,53,482,806,571,748,850,167,94,250,427,814,417,790,228,23,381,181,912,189,62,310,860,621,908,770,978,216,865,801,765,948,784,766,611,890,377,789,643,489,186,633,851,554,385,470,644,615,860,4,65,760,472,604,370,463,740,791,19,195,674,597,768,815,665,257,516,752,536,472,215,784,718,872,974,985,294,633,90,953,717,962,774,769,902,613,562,731,159,770,434,961,767,969,863,74,468,484,48,327,13,939,24,274,877,187,507,108,878,963,6,830,724,288,924,820,349,757,20,879,579,353,545,488,510,641,294,230,886,149,937,919,82,243,694,513,832,862,20,99,755,995,443,599,691,501,356,8,529,849,369,649,296,288,952,457,809,759,840,66,956,389,513,789,867,258,583,371,602,642,192,803,633,479,684,311,347,195,150,193,231,769,318,486,138,591,574,423,727,76,572,567,969,603,191,839,514,329,543,558,26,679,645,353,259,235,6,601,927,446,952,605,164,886,571,787,188,438,434,387,233,935,13,194,503,526,327,268,358,181,456,59,104,331,967,157,438,29,526,841,606,680,134,790,41,725,909,142,906,929,777,992,399,879,175,849,895,832,653,110,411,304,334,858,179,259,376,456,374,890,220,255,588,376,131,901,199,487,884,244,828,108,598,737,559,888,529,691,677,253,14,676,402,137,671,679,943,363,87,810,991,771,497,603,793,206,983,627,252,70,944,512,505,849,447,619,896,995,852,911,30,953,102,893,541,587,980,513,977,854,830,508,642,829,651,28,69,589,39,981,724,719,604,756,745,611,139,974,713,852,799,576,227,514,621,917,593,133,177,932,803,176,629,162,411,385,264,338,944,784,601,717,708,539,995,234,389,369,291,289,767,658,576,144,150,198,715,496,331,708,988,340,476,885,644,624,710,40,675,116,767,45,573,112,781,537,459,363,52,696,808,697,474,758,586,828,873,150,945,450,994,251,948,968,576,134,638,979,850,727,281,171,978,445,355,769,826,489,72,308,421,122,248,487,227,569,961,502,511,338,919,915,879,357,354,788,852,272,493,185,784,511,593,888,649,767,690,673,491,246,327,110,936,767,666,954,185,930,708,700,293,920,260,746,92,826,433,532,304,55,352,148,895,843,136,459,943,99,993,418,644,402,552,835,882,627,541,930,256,559,279,177,232,153,957,907,297,236,585,118,65,897,91,637,338,601,835,303,693,781,315,383,121,742,613,564,592,280,161,626,190,438,29,585,100,72,893,300,968,613,711,308,416,111,318,951,207,446,898,375,967,821,31,164,511,204,1000,960,614,322,698,20,862,821,24,547,96,969,239,668,19,651,970,421,565,178,475,403,963,896,44,843,487,183,449,105,172,41,772,558,558,65,561,321,471,565,527,624,566,710,855,338,763,475,450,443,901,522,166,231,113,296,88,26,761,248,617,954,163,793,356,235,60,750,636,852,192,513,431,83,953,499,176,243,483,750,179,458,318,861,688,263,604,380,522,989,303,16,954,445,461,795,451,787,245,40,129,496,103,275,594,717,235,251,496,35,191,63,68,547,321,281,513,31,10,485,755,339,999,136,650,743,18,192,201,39,244,901,146,334,445,116,337,200,806,272,499,898,28,197,740,174,487,342,409,780,483,72,715,667,864,339,479,315,261,950,198,925,475,679,361,168,266,347,567,267,356,358,526,745,535,697,189,947,787,989,561,967,164,198,634,414,217,317,911,383,701,858,809,669,521,100,483,181,310,314,553,147,373,39,787,125,252,392,731,663,761,157,604,555,902,845,451,676,526,692,880,709,96,467,802,831,134,31,121,434,162,784,577,118,101,360,538,625,290,544,425,347,147,88,332,570,562,158,668,680,960,285,795,663,995,580,77,212,921,503,745,312,804,645,238,3,146,934,736,921,922,217,27,724,856,943,360,973,389,858,315,190,939,405,161,438,273,459,327,437,199,658,79,26,191,553,173,429,948,996,790,947,619,864,736,20,568,808,289,481,893,853,642,542,243,318,853,321,998,685,967,473,813,75,239,286,467,392,972,443,499,383,895,376,31,332,609,822,636,464,679,881,468,243,81,878,619,739,700,856,346,21,829,549,131,522,877,18,876,905,512,317,406,706,271,554,679,182,521,420,983,317,317,952,676,241,346,208,735,955,331,510,250,52,918,36,845,840,618,588,135,121,282,1000,977,16,150,35,791,93,363,986,61,567,307,653,837,421,741,180,527,729,581,348,539,275,143,360,840,998,812,808,170,173,458,439,38,619,701,842,136,355,762,199,246,494,763,140,535,951,761,374,593,875,456,34,423,798,148,783,788,322,22,301,454,151,940,5,532,929,938,405,681,473,622,811,806,856,641,230,693,810,423,29,326,310,623,990,804,889,36,562,169,168,100,267,270,981,422,237,223,31,521,791,250,570,984,186,504,356,154,599,488,305,454,616,507,660,501,707,613,44,502,785,737,719,589,214,927,715,493,906,888,559,972,457,994,188,111,900,257,715,781,513,563,306,555,768,860,205,191,655,42,10,163,233,509,664,359,39,905,305,578,958,662,563,542,78,614,459,46,105,423,805,73,348,453,596,264,348,501,128,837,233,82,823,79,78,73,854,555,55,228,598,527,708,633,931,315,801,858,219,33,769,225,602,782,662,253,574,315,138,950,605,734,893,11,672,487,833,962,92,404,758,448,701,448,283,961,391,577,708,675,932,824,871,658,275,696,306,253,523,349,494,978,859,320,797,746,62,369,576,557,695,891,484,306,370,757,372,148,943,566,890,238,337,201,418,510,433,926,738,766,624,844,789,851,234,990,214,536,629,972,888,613,560,678,237,669,247,748,556,618,727,820,533,871,202,217,854,482,255,633,714,826,69,813,160,374,996,444,925,62,441,21,466,131,548,106,715,725,937,292,276,907,660,476,9,981,207,136,53,710,865,759,382,190,405,433,468,987,390,176,848,495,319,675,988,556,887,246,813,242,625,630,650,136,960,10,889,373,389,463,595,67,198,907,141,692,687,315,593,549,510,567,695,804,320,934,70,792,346,764,566,35,406,644,322,899,473,707,158,965,356,195,738,193,148,15,459,443,496,734,720,314,284,386,776,685,65,177,167,598,18,349,779,428,699,566,302,362,707,672,692,649,894,361,93,771,998,671,974,206,864,2,676,406,923,448,67,562,102,191,598,25,740,513,418,441,316,107,863,931,629,912,741,635,439,792,226,889,144,546,637,538,20,252,847,280,414,315,361,438,989,696,752,533,127,636,5,581,179,73,848,734,48,765,616,787,262,393,247,682,532,972,259,351,789,5,602,766,681,680,763,659,765,357,544,28,823,68,803,959,320,89,345,197,509,668,383,949,400,603,730,709,126,398,736,236,40,340,126,271,779,964,650,842,783,345,861,575,251,843,58,64,797,410,386,938,694,571,968,727,534,876,571,555,930,370,831,383,951,620,353,186,857,305,733,858,429,368,410,280,168,432,762,405,891,489,674,620,58,480,541,848,130,389,521,983,568,741,156,178,851,144,278,438,712,105,812,747,824,866,293,731,908,629,679,967,591,104,961,732,548,628,902,840,940,264,641,928,163,580,293,865,571,328,542,286,488,373,82,182,143,967,227,87,808,467,648,422,489,408,620,511,98,4,598,448,334,816,366,687,783,804,249,363,494,943,581,651,843,442,15,332,16,80,992,167,909,167,559,322,79,252,739,152,267,809,460,789,142,116,970,554,508,850,152,433,860,63,134,909,584,680,693,541,730,107,840,706,502,641,731,488,338,712,405,364,112,585,758,214,360,672,786,277,991,767,18,39,986,158,644,69,870,930,737,385,311,736,65,46,48,916,627,54,669,58,851,229,553,873,733,56,646,651,264,145,650,296,432,257,992,308,960,298,25,541,73,660,792,140,945,633,396,482,775,501,801,108,856,415,99,324,10,521,906,378,464,413,776,594,596,409,936,726,119,711,701,9,861,956,959,393,734,833,317,297,175,853,831,653,329,471,992,166,647,241,162,789,692,463,611,474,203,206,332,690,85,61,813,351,66,777,771,807,366,812,533,382,636,556,528,423,811,743,421,395,612,676,631,136,67,169,892,117,561,905,191,290,630,134,779,661,612,21,749,646,520,324,39,824,872,612,809,951,421,397,698,589,102,797,521,473,166,825,81,720,791,322,626,507,923,174,757,155,169,386,294,425,269,494,518,559,545,298,99,406,55,982,412,430,931,427,389,369,881,756,25,786,940,342,657,824,233,316,603,278,427,442,892,171,899,552,4,132,182,930,911,88,639,83,75,542,557,44,38,20,528,52,979,32,44,827,42,416,940,228,100,492,652,105,468,8,839,857,332,252,684,504,576,915,296,263,437,784,196,261,827,866,884,247,399,462,777,6,899,13,293,971,55,223,644,723,88,516,753,754,62,242,296,764,932,485,500,49,930,114,989,859,825,868,397,284,656,654,742,625,390,467,175,699,745,292,994,134,645,976,501,538,464,972,290,584,969,416,679,775,536,324,427,175,454,884,858,179,934,782,429,317,745,640,423,734,389,358,920,458,3,359,227,395,606,924,710,104,731,801,230,776,682,956,901,536,52,710,810,995,157,788,662,688,334,483,810,465,64,730,689,661,739,613,532,482,643,209,725,475,729,977,523,968,863,755,301,834,78,997,924,793,609,373,587,642,951,400,790,759,380,65,536,522,857,990,27,605,888,81,392,415,521,88,360,456,451,154,142,342,377,583,473,53,577,605,7]
    k = 1440
    ans = s.maxScore(cards, k)
    print(ans)



