! function (a) {
    function e(e) {
        for (var i, c, l = e[0], r = e[1], o = e[2], v = 0, p = []; v < l.length; v++) c = l[v], Object.prototype.hasOwnProperty.call(n, c) && n[c] && p.push(n[c][0]), n[c] = 0;
        for (i in r) Object.prototype.hasOwnProperty.call(r, i) && (a[i] = r[i]);
        for (d && d(e); p.length;) p.shift()();
        return s.push.apply(s, o || []), t()
    }

    function t() {
        for (var a, e = 0; e < s.length; e++) {
            for (var t = s[e], i = !0, l = 1; l < t.length; l++) {
                var r = t[l];
                0 !== n[r] && (i = !1)
            }
            i && (s.splice(e--, 1), a = c(c.s = t[0]))
        }
        return a
    }
    var i = {},
        n = {
            0: 0
        },
        s = [];

    function c(e) {
        if (i[e]) return i[e].exports;
        var t = i[e] = {
            i: e,
            l: !1,
            exports: {}
        };
        return a[e].call(t.exports, t, t.exports, c), t.l = !0, t.exports
    }
    c.m = a, c.c = i, c.d = function (a, e, t) {
        c.o(a, e) || Object.defineProperty(a, e, {
            enumerable: !0,
            get: t
        })
    }, c.r = function (a) {
        "undefined" != typeof Symbol && Symbol.toStringTag && Object.defineProperty(a, Symbol.toStringTag, {
            value: "Module"
        }), Object.defineProperty(a, "__esModule", {
            value: !0
        })
    }, c.t = function (a, e) {
        if (1 & e && (a = c(a)), 8 & e) return a;
        if (4 & e && "object" == typeof a && a && a.__esModule) return a;
        var t = Object.create(null);
        if (c.r(t), Object.defineProperty(t, "default", {
                enumerable: !0,
                value: a
            }), 2 & e && "string" != typeof a)
            for (var i in a) c.d(t, i, function (e) {
                return a[e]
            }.bind(null, i));
        return t
    }, c.n = function (a) {
        var e = a && a.__esModule ? function () {
            return a.default
        } : function () {
            return a
        };
        return c.d(e, "a", e), e
    }, c.o = function (a, e) {
        return Object.prototype.hasOwnProperty.call(a, e)
    }, c.p = "/";
    var l = window.webpackJsonp = window.webpackJsonp || [],
        r = l.push.bind(l);
    l.push = e, l = l.slice();
    for (var o = 0; o < l.length; o++) e(l[o]);
    var d = r;
    s.push([141, 2]), t()
}({
    141: function (a, e, t) {
        "use strict";
        t.r(e),
            function (a) {
                t(142), t(148), t(150), t(151), t(152);
                a(window).width() > 768 ? a(".for-mobile").each((function () {
                    this.remove()
                })) : a(".for-desktop").each((function () {
                    this.remove()
                })), a(".m-side-toggler").on("click", (function (e) {
                    return e.preventDefault(), e.stopPropagation(), a(".m-side").toggleClass("show"), a(".backdrop").toggleClass("show"), !1
                })), a(".backdrop").on("click", (function () {
                    a(".m-side").removeClass("show"), a(".backdrop").removeClass("show")
                })), a(".m-search-toggler").on("click", (function (e) {
                    return e.preventDefault(), e.stopPropagation(), a(".m-header-logo").toggleClass("hide"), a(".m-header-search").toggleClass("show"), a(".m-header-search").hasClass("show") && a(".m-header-search .js-search").focus(), !1
                })), a(document).on("click", ".spoiler__header", (function () {
                    a(this).closest(".spoiler").toggleClass("open")
                })), a(document).on("click", "a.spoiler__title", (function (a) {
                    return a.stopPropagation(), !0
                })), a(document).on("click", ".js-tab", (function () {
                    if (a(this).siblings(".js-tab").removeClass("active"), a(this).addClass("active"), this.dataset.target) {
                        var e = a(this.dataset.target);
                        e.siblings().removeClass("active"), e.addClass("active")
                    }
                }))
            }.call(this, t(1))
    },
    148: function (a, e, t) {
        var i = t(3),
            n = t(149);
        "string" == typeof (n = n.__esModule ? n.default : n) && (n = [
            [a.i, n, ""]
        ]);
        var s = {
            insert: "head",
            singleton: !1
        };
        i(n, s);
        a.exports = n.locals || {}
    },
    149: function (a, e, t) {},
    150: function (a, e) {
        _APP.api = "".concat(location.protocol, "//").concat(location.hostname, "/api"), _APP.football = {
            url: {
                root: "/football",
                game: "/football/match",
                team: "/football/team"
            },
            prefix: "f",
            numberPeriods: 2,
            color: {
                statistic: ["#c4c4c4", "var(--green)"]
            }
        }, _APP.hockey = {
            url: {
                root: "/hockey",
                game: "/hockey/match",
                team: "/hockey/team"
            },
            prefix: "h",
            numberPeriods: 3,
            color: {
                statistic: ["#c4c4c4", "var(--blue)"]
            }
        }, _APP.scheme = {
            statistic: {
                1: [0, 1],
                2: [0, 1],
                3: [0, 1],
                4: [0, 1],
                5: [0, 1],
                6: [0, 1],
                7: [1, 1],
                8: [0, 1],
                9: [0, 1],
                10: [0, 1],
                11: [1, 0],
                12: [1, 0],
                13: [1, 0],
                14: [0, 1],
                15: [0, 1],
                16: [0, 1],
                17: [0, 1],
                18: [0, 1],
                19: [0, 1],
                20: [0, 1],
                21: [0, 1]
            },
            football: {
                series: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 29, 30, 31, 32, 27, 28, 33, 34, 35, 36]
            },
            hockey: {
                series: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52]
            }
        }
    },
    151: function (a, e, t) {
        (function (a) {
            a(".spoiler-countries-more").on("click", (function () {
                var e = a(this).closest(".spoiler-countries"),
                    t = this;
                t.disabled = !0, a(this).addClass("loading");
                var i = {
                    action: "countries",
                    offset: 20
                };
                "football" == _APP.controller ? i.football = 1 : "hockey" == _APP.controller && (i.hockey = 1), a.ajax({
                    data: JSON.stringify(i),
                    url: _APP.api + "/country",
                    type: "POST",
                    dataType: "JSON",
                    success: function (a) {
                        try {
                            if (!a) return;
                            var i = "";
                            a.forEach((function (a) {
                                i += '<div class="spoiler spoiler-tournaments">\n              <div class="spoiler__header js-get-tournaments" data-id="'.concat(a.cId, '" data-alias="').concat(a.cA, '">\n                <div class="spoiler__title">\n                  <span class="spoiler__title-icon flag flag-').concat(a.cId, '"></span>\n                  ').concat(a.cT, '\n                </div>\n              </div>\n              <div class="spoiler__body">\n              </div>\n            </div>')
                            })), e.children(".spoiler__body").append(i), t.remove()
                        } catch (a) {
                            console.log(a)
                        }
                    }
                })
            })), a(".spoiler-countries").on("click", ".js-get-tournaments", (function () {
                var e = a(this).closest(".spoiler-tournaments");
                if (!e.hasClass("loaded")) {
                    for (var t = '<div class="list list_bg_gray">', i = 0; i < 5; i++) t += '<span class="list__item"><span class="loading-content"></span></span>';
                    t += "</div>", e.children(".spoiler__body").html(t);
                    var n = this.dataset.alias,
                        s = {
                            action: "tournaments",
                            cId: this.dataset.id
                        };
                    a.ajax({
                        data: JSON.stringify(s),
                        url: _APP.api + "/" + _APP.controller,
                        type: "POST",
                        dataType: "JSON",
                        success: function (a) {
                            try {
                                if (!a) return;
                                var t = '<div class="list list_bg_gray">';
                                a.forEach((function (a) {
                                    t += '<a class="list__item" href="'.concat(_APP[_APP.controller].url.root, "/").concat(n, "/").concat(a.tIDH, '">').concat(a.tT, "</a>")
                                })), t += "</div>", e.children(".spoiler__body").html(t), e.addClass("loaded")
                            } catch (a) {
                                console.log(a)
                            }
                        }
                    })
                }
            }))
        }).call(this, t(1))
    },
    152: function (a, e, t) {
        "use strict";
        (function (a) {
            var e = t(0),
                i = t.n(e),
                n = t(2);
            if (a.datepicker.setDefaults({
                    closeText: "Закрыть",
                    prevText: "&#x3C;Пред",
                    nextText: "След&#x3E;",
                    currentText: "Сегодня",
                    monthNames: ["Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"],
                    monthNamesShort: ["Янв", "Фев", "Мар", "Апр", "Май", "Июн", "Июл", "Авг", "Сен", "Окт", "Ноя", "Дек"],
                    dayNames: ["воскресенье", "понедельник", "вторник", "среда", "четверг", "пятница", "суббота"],
                    dayNamesShort: ["вск", "пнд", "втр", "срд", "чтв", "птн", "сбт"],
                    dayNamesMin: ["Вс", "Пн", "Вт", "Ср", "Чт", "Пт", "Сб"],
                    weekHeader: "Нед",
                    dateFormat: "dd.mm.yy",
                    firstDay: 1,
                    isRTL: !1,
                    showMonthAfterYear: !1,
                    yearSuffix: ""
                }), a.datepicker._generateMonthYearHeader = function (a, e, t, i, n, s, c, l) {
                    var r, o, d, v, p, _, h, m, u = this._get(a, "changeMonth"),
                        g = this._get(a, "changeYear"),
                        f = this._get(a, "showMonthAfterYear"),
                        P = '<div class="ui-datepicker-title">',
                        w = "",
                        y = "";
                    r = i && i.getFullYear() === t, o = n && n.getFullYear() === t, w += '<div class="ui-datepicker-select ui-datepicker-select-month"><select class="ui-datepicker-select__input ui-datepicker-month" data-handler="selectMonth" data-event="change">';
                    var b = "";
                    for (d = 0; d < 12; d++)
                        if ((!r || d >= i.getMonth()) && (!o || d <= n.getMonth())) {
                            w += '<option value="' + d + '"';
                            var j = '<div data-value="' + d + '" class="ui-datepicker-dropdown__item';
                            d === e && (w += ' selected="selected"', j += " active", y = c[d]), w += ">" + c[d] + "</option>", b += j += '">' + c[d] + "</div>"
                        } if (w += '</select><div class="ui-datepicker-select__value">' + y + '</div><div class="ui-datepicker-dropdown hidden">' + b + "</div></div>", f || (P += w + (!s && u && g ? "" : "&#xa0;")), !a.yearshtml) {
                        a.yearshtml = "";
                        var R = "";
                        v = this._get(a, "yearRange").split(":"), p = (new Date).getFullYear(), h = (_ = function (a) {
                            var e = a.match(/c[+\-].*/) ? t + parseInt(a.substring(1), 10) : a.match(/[+\-].*/) ? p + parseInt(a, 10) : parseInt(a, 10);
                            return isNaN(e) ? p : e
                        })(v[0]), m = Math.max(h, _(v[1] || "")), h = i ? Math.max(h, i.getFullYear()) : h, m = n ? Math.min(m, n.getFullYear()) : m, a.yearshtml += '<div class="ui-datepicker-select ui-datepicker-select-year"><select class="ui-datepicker-select__input" data-handler="selectYear" data-event="change">';
                        for (var A = []; h <= m; h++) {
                            a.yearshtml += '<option value="' + h + '"';
                            var k = '<div data-value="' + h + '" class="ui-datepicker-dropdown__item';
                            h === t && (a.yearshtml += ' selected="selected"', k += " active", R = h), a.yearshtml += ">" + h + "</option>", k += '">' + h + "</div>", A.push(k)
                        }
                        a.yearshtml += '</select><div class="ui-datepicker-select__value">' + R + '</div><div class="ui-datepicker-dropdown hidden">' + A.reverse().join("") + "</div></div>", P += a.yearshtml, a.yearshtml = null
                    }
                    return P += this._get(a, "yearSuffix"), f && (P += (!s && u && g ? "" : "&#xa0;") + w), P += "</div>"
                }, a(document).on("click", ".ui-datepicker-select__value", (function () {
                    a(this).siblings(".ui-datepicker-dropdown").toggleClass("hidden")
                })), a(document).on("click", ".ui-datepicker-select-month .ui-datepicker-select__value", (function () {
                    a(".ui-datepicker-select-year .ui-datepicker-dropdown").addClass("hidden")
                })), a(document).on("click", ".ui-datepicker-select-year .ui-datepicker-select__value", (function () {
                    a(".ui-datepicker-select-month .ui-datepicker-dropdown").addClass("hidden")
                })), a(document).on("click", ".ui-datepicker-dropdown__item", (function () {
                    a(this).siblings().removeClass("active"), a(this).addClass("active");
                    var e = a(this).closest(".ui-datepicker-select");
                    e.find(".ui-datepicker-select__value").text(this.innerText), e.find(".ui-datepicker-select__input").val(this.dataset.value).trigger("change")
                })), a(".date-games").each((function () {
                    var e = a(this),
                        t = a(this).parent(),
                        n = t.find(".btn-calendar__selected-value");
                    e.datepicker({
                        dateFormat: "yy-mm-dd",
                        maxDate: i()().toDate(),
                        minDate: "-20y",
                        showOtherMonths: !0,
                        yearRange: "-20:+0",
                        beforeShow: function (e, i) {
                            t.addClass("active"), a(".ui-datepicker").attr("data-id", e.id)
                        },
                        onSelect: function (a, e) {
                            a = i()(a), n && n.text(a.format("DD/MM") + " " + _T.daysWeek[a.day()]), document.querySelector(".events-data-date").changeValue(a.format("YYYY-MM-DD"))
                        },
                        onClose: function () {
                            t.removeClass("active")
                        }
                    })
                })), a(".events").on("click", ".event", (function (e) {
                    return a(window).width() <= 1500 || (e.preventDefault(), a(".event.active").removeClass("active"), a(this).addClass("active"), document.querySelector(".review-data-idh").changeValue(this.dataset.idh), !1)
                })), a("body").hasClass("game")) {
                if (window.detailRes && a("#game-detail").html(function (e) {
                        var t, i = ["soccer-ball", "soccer-ball-own", "hockey-ball", "y-card", "r-card", "yr-card", "substitution", "substitution-in", "substitution-out", "lineup1", "lineup0", "penalty", "penalty-missed", "attendance", "question", "hockey-penalty-2", "hockey-penalty-5", "hockey-penalty-10", "hockey-penalty-game-misconduct", "injury", "unsure", "time", "commentary", "announcement", "whistle", "corner", "funfact", "exclamation", "sadness", "live-offer1"],
                            n = ["participant-name", "substitution-in-name", "substitution-out-name"],
                            s = ["note-name span"],
                            c = "",
                            l = [];
                        a(e.D).each((function () {
                            var e = a(this);
                            if (e.hasClass("detailMS__incidentsHeader")) e.find(".detailMS__headerText").length && (t = parseInt(e.find(".detailMS__headerText").text()), l[t] = []);
                            else if (e.hasClass("incidentRow--home")) {
                                var c = '<div class="detail-event detail-event_home">',
                                    r = e.find(".time-box");
                                if (r && r.length) c += '<div class="detail-event__time">' + r.html() + "</div>";
                                else {
                                    var o = e.find(".time-box-wide");
                                    o && o.length ? c += '<div class="detail-event__time">' + o.html() + "</div>" : c += '<div class="detail-event__time"></div>'
                                }
                                c += '<div class="detail-event__icon">', i.forEach((function (a) {
                                    var t = e.find("." + a);
                                    t && t.length && (c += '<span class="icon icon-detail icon-'.concat(a, '"></span>'))
                                })), c += "</div>", c += '<div class="detail-event__player">', n.forEach((function (a) {
                                    var t = e.find("." + a);
                                    t && t.length && (c += '<span class="'.concat(a, '">').concat(t.text(), "</span>"))
                                })), s.forEach((function (a) {
                                    var t = e.find("." + a);
                                    t && t.length && (c += '<span class="'.concat(a, '">(').concat(t.text(), ")</span>"))
                                })), c += "</div>", c += "</div>", l[t].push({
                                    H: c
                                })
                            } else if (e.hasClass("incidentRow--away")) {
                                var d = '<div class="detail-event detail-event_away">',
                                    v = e.find(".time-box");
                                if (v && v.length) d += '<div class="detail-event__time">' + v.html() + "</div>";
                                else {
                                    var p = e.find(".time-box-wide");
                                    p && p.length ? d += '<div class="detail-event__time">' + p.html() + "</div>" : d += '<div class="detail-event__time"></div>'
                                }
                                d += '<div class="detail-event__icon">', i.forEach((function (a) {
                                    var t = e.find("." + a);
                                    t && t.length && (d += '<span class="icon icon-detail icon-'.concat(a, '"></span>'))
                                })), d += "</div>", d += '<div class="detail-event__player">', n.forEach((function (a) {
                                    var t = e.find("." + a);
                                    t && t.length && (d += '<span class="'.concat(a, '">').concat(t.text(), "</span>"))
                                })), s.forEach((function (a) {
                                    var t = e.find("." + a);
                                    t && t.length && (d += '<span class="'.concat(a, '">(').concat(t.text(), ")</span>"))
                                })), d += "</div>", d += "</div>", l[t].push({
                                    A: d
                                })
                            }
                        }));
                        for (var r = 1; r <= _APP[_APP.controller].numberPeriods; r++) l[r] && (c += '<div class="detail-period">\n          <div class="detail-period__title">'.concat(r, " ").concat(_T[_APP.controller].period, '</div>\n            <div class="detail-card">\n              <div class="detail-card__body">'), l[r].forEach((function (a) {
                            a.H && (c += a.H), a.A && (c += a.A)
                        })), c += "</div></div></div>");
                        return c
                    }(window.detailRes)), a(window).width() > 1500 ? (a(".middle-left .review-nav .nav__tab-statistic").remove(), a(".middle-left .review-nav .nav__tab-lineups").remove(), a(".middle-left .review-subnav .nav-statistic").remove(), a(".middle-left #game-statistic").remove(), a(".middle-left #game-lineups").remove()) : a(".middle-right .mr-review").remove(), window.statisticRes) {
                    var s = a("#game-statistic");
                    if (s) {
                        s.html(p(window.statisticRes));
                        var c = s.find(".nav-statistic .nav__tab").first();
                        c.addClass("active"), s.find(c.attr("data-target")).addClass("active")
                    }
                    if (s = a("#mr-game-statistic")) {
                        s.html(p(window.statisticRes, "mr-"));
                        var l = s.find(".mr-nav-statistic .nav__tab").first();
                        l.addClass("active"), s.find(l.attr("data-target")).addClass("active")
                    }
                }
                if (window.lineupsRes) {
                    var r = a("#game-lineups");
                    if (r)
                        if (a(window).width() <= 768) {
                            var o = a(_(window.lineupsRes));
                            o.find("tr").first().after('<tr><td class="h-part summary-vertical fl">' + o.find(".lineups-header__participant_home").text() + '</td><td class="h-part summary-vertical fr">' + o.find(".lineups-header__participant_away").text() + "</td></tr>"), r.html(o), r.find(".lineups-header").remove()
                        } else r.html(_(window.lineupsRes));
                    (r = a("#mr-game-lineups")) && r.html(_(window.lineupsRes))
                }
            }

            function d() {
                var e = a(this.dataset.target).find(".spoiler-h2h-".concat(this.dataset.section)),
                    t = e.find(".event-h2h:not(.show)");
                t && t.length && (t.slice(0, 5).addClass("show"), (t = e.find(".event-h2h:not(.show)")) && t.length || e.find(".js-h2h-more").remove())
            }

            function v(e) {
                var t, i = ["soccer-ball", "soccer-ball-own", "hockey-ball", "y-card", "r-card", "yr-card", "substitution", "substitution-in", "substitution-out", "lineup1", "lineup0", "penalty", "penalty-missed", "attendance", "question", "hockey-penalty-2", "hockey-penalty-5", "hockey-penalty-10", "hockey-penalty-game-misconduct", "injury", "unsure", "time", "commentary", "announcement", "whistle", "corner", "funfact", "exclamation", "sadness", "live-offer1"],
                    n = ["participant-name", "substitution-in-name", "substitution-out-name"],
                    s = ["note-name span"],
                    c = "",
                    l = [];
                a(e.D).each((function () {
                    var e = a(this);
                    if (e.hasClass("detailMS__incidentsHeader")) e.find(".detailMS__headerText").length && (t = parseInt(e.find(".detailMS__headerText").text()), l[t] = {
                        H: [],
                        A: []
                    });
                    else if (e.hasClass("incidentRow--home")) {
                        var c = '<div class="detail-event">',
                            r = e.find(".time-box");
                        if (r && r.length) c += '<div class="detail-event__time">' + r.html() + "</div>";
                        else {
                            var o = e.find(".time-box-wide");
                            o && o.length ? c += '<div class="detail-event__time">' + o.html() + "</div>" : c += '<div class="detail-event__time"></div>'
                        }
                        c += '<div class="detail-event__icon">', i.forEach((function (a) {
                            var t = e.find("." + a);
                            t && t.length && (c += '<span class="icon icon-detail icon-'.concat(a, '"></span>'))
                        })), c += "</div>", c += '<div class="detail-event__player">', n.forEach((function (a) {
                            var t = e.find("." + a);
                            t && t.length && (c += '<span class="'.concat(a, '">').concat(t.text(), "</span>"))
                        })), s.forEach((function (a) {
                            var t = e.find("." + a);
                            t && t.length && (c += '<span class="'.concat(a, '">(').concat(t.text(), ")</span>"))
                        })), c += "</div>", c += "</div>", l[t].H.push(c)
                    } else if (e.hasClass("incidentRow--away")) {
                        var d = '<div class="detail-event">',
                            v = e.find(".time-box");
                        if (v && v.length) d += '<div class="detail-event__time">' + v.html() + "</div>";
                        else {
                            var p = e.find(".time-box-wide");
                            p && p.length ? d += '<div class="detail-event__time">' + p.html() + "</div>" : d += '<div class="detail-event__time"></div>'
                        }
                        d += '<div class="detail-event__icon">', i.forEach((function (a) {
                            var t = e.find("." + a);
                            t && t.length && (d += '<span class="icon icon-detail icon-'.concat(a, '"></span>'))
                        })), d += "</div>", d += '<div class="detail-event__player">', n.forEach((function (a) {
                            var t = e.find("." + a);
                            t && t.length && (d += '<span class="'.concat(a, '">').concat(t.text(), "</span>"))
                        })), s.forEach((function (a) {
                            var t = e.find("." + a);
                            t && t.length && (d += '<span class="'.concat(a, '">(').concat(t.text(), ")</span>"))
                        })), d += "</div>", d += "</div>", l[t].A.push(d)
                    }
                }));
                for (var r = 1; r <= _APP[_APP.controller].numberPeriods; r++)
                    if (l[r]) {
                        var o = "";
                        l[r].H && l[r].H.length && l[r].H.forEach((function (a) {
                            o += a
                        }));
                        var d = "";
                        l[r].A && l[r].A.length && l[r].A.forEach((function (a) {
                            d += a
                        })), c += '<div class="detail-period detail-period_small">\n          <div class="detail-period__title">'.concat(r, " ").concat(_T[_APP.controller].period, '</div>\n          <div class="detail-period__participants">\n            <div class="detail-period__participant detail-period__participant_home">\n              <div class="detail-card detail-card_small">\n                <div class="detail-card__header">\n                  <div class="detail-card__cell detail-card__time"><img class="icon icon-clock" src="images/icons/icon-clock-gray.svg"></div>\n                  <div class="detail-card__cell detail-card__icon"><img class="icon icon-whistle" src="images/icons/icon-whistle-gray.svg"></div>\n                  <div class="detail-card__cell detail-card__player"><img class="icon icon-person" src="images/icons/icon-person-gray.svg"></div>\n                </div>\n                <div class="detail-card__body">').concat(o, '</div>\n              </div>\n            </div>\n            <div class="detail-period__participant detail-period__participant_away">\n              <div class="detail-card detail-card_small">\n                <div class="detail-card__header">\n                  <div class="detail-card__cell detail-card__time"><img class="icon icon-clock" src="images/icons/icon-clock-gray.svg"></div>\n                  <div class="detail-card__cell detail-card__icon"><img class="icon icon-whistle" src="images/icons/icon-whistle-gray.svg"></div>\n                  <div class="detail-card__cell detail-card__player"><img class="icon icon-person" src="images/icons/icon-person-gray.svg"></div>\n                </div>\n                <div class="detail-card__body">').concat(d, "</div>\n              </div>\n            </div>\n          </div>\n        </div>")
                    } return c
            }

            function p(a) {
                var e = arguments.length > 1 && void 0 !== arguments[1] ? arguments[1] : "",
                    t = {
                        G: "",
                        P1: "",
                        P2: "",
                        P3: "",
                        O: ""
                    };
                ["G", "P1", "P2", "P3", "O"].forEach((function (e) {
                    for (var i in a[e])(a[e][i].H || a[e][i].A) && (t[e] += n(i, a[e][i].H, a[e][i].A))
                }));
                var i = '<div class="'.concat(e, 'statistic-nav"><div class="').concat(e, 'nav-statistic nav">');
                return t.G.length && (i += '<a class="nav__tab btn-link js-tab" href="javascript:void(0)" data-target="#'.concat(e, "statistic-g\" onclick=\"document.querySelector('.statistic-data-tab').changeValue('g')\"><span>Матч</span></a>")), t.P1.length && (i += '<a class="nav__tab btn-link js-tab" href="javascript:void(0)" data-target="#'.concat(e, "statistic-p1\" onclick=\"document.querySelector('.statistic-data-tab').changeValue('p1')\"><span>1 ").concat(_T[_APP.controller].period, "</span></a>")), t.P2.length && (i += '<a class="nav__tab btn-link js-tab" href="javascript:void(0)" data-target="#'.concat(e, "statistic-p2\" onclick=\"document.querySelector('.statistic-data-tab').changeValue('p2')\"><span>2 ").concat(_T[_APP.controller].period, "</span></a>")), t.P3.length && (i += '<a class="nav__tab btn-link js-tab" href="javascript:void(0)" data-target="#'.concat(e, "statistic-p3\" onclick=\"document.querySelector('.statistic-data-tab').changeValue('p3')\"><span>3 ").concat(_T[_APP.controller].period, "</span></a>")), t.O.length && (i += '<a class="nav__tab btn-link js-tab" href="javascript:void(0)" data-target="#'.concat(e, "statistic-o\" onclick=\"document.querySelector('.statistic-data-tab').changeValue('o')\"><span>Дополнительное время</span></a>")), i += '</div></div><div class="statistic-contents">', t.G.length && (i += '<div id="'.concat(e, 'statistic-g" class="statistic-content">').concat(t.G, "</div>")), t.P1.length && (i += '<div id="'.concat(e, 'statistic-p1" class="statistic-content">').concat(t.P1, "</div>")), t.P2.length && (i += '<div id="'.concat(e, 'statistic-p2" class="statistic-content">').concat(t.P2, "</div>")), t.P3.length && (i += '<div id="'.concat(e, 'statistic-p3" class="statistic-content">').concat(t.P3, "</div>")), t.O.length && (i += '<div id="'.concat(e, 'statistic-o" class="statistic-content">').concat(t.O, "</div>")), i += "</div>";

                function n(a, e, t) {
                    var i = 100 * (e = parseInt(e)) / (e + (t = parseInt(t))),
                        n = 100 - i;
                    return [1].indexOf(a) > -1 && (e += "%", t += "%"), '<div class="statistic-row">\n      <div class="statistic-text-group">\n        <div class="statistic-text statistic-text_home">'.concat(e, '</div>\n        <div class="statistic-text statistic-text_title">').concat(_T[_APP.controller].statistic[a], '</div>\n        <div class="statistic-text statistic-text_away">').concat(t, '</div>\n      </div>\n      <div class="statistic-bar-group">\n        <div class="statistic-bar statistic-bar_home">\n          <div class="statistic-bar-bg">\n            <div class="statistic-bar-line" style="width:').concat(i, "%;background-color:").concat(_APP[_APP.controller].color.statistic[_APP.scheme.statistic[a][0]], '"></div>\n          </div>\n        </div>\n        <div class="statistic-bar statistic-bar_away">\n          <div class="statistic-bar-bg">\n            <div class="statistic-bar-line" style="width:').concat(n, "%;background-color:").concat(_APP[_APP.controller].color.statistic[_APP.scheme.statistic[a][1]], '"></div>\n          </div>\n        </div>\n      </div>\n    </div>')
                }
            }

            function _(a) {
                var e = "";
                return (a.HP && a.AP || a.L) && (a.HP && a.AP && (e += '<div class="lineups-header">\n          <div class="lineups-header__participant lineups-header__participant_home">'.concat(a.HP, '</div>\n          <div class="lineups-header__title">Расстановка</div>\n          <div class="lineups-header__participant lineups-header__participant_away">').concat(a.AP, "</div>\n        </div>")), a.L && (e += '<table class="lineups-table">'.concat(a.L, "</table>"))), e
            }

            function h() {
                for (var a = "", e = 0; e < 2; e++) {
                    a += '<div class="spoiler spoiler-h2h spoiler-h2h-h open"><div class="spoiler__header"><span class="spoiler__title"><span class="loading-content" style="width:160px;"></span></span></div><div class="spoiler__body">';
                    for (var t = 0; t < 5; t++) a += '<a class="event event-game event-h2h show" href="javascript:void(0)">\n      <div class="event__cell event__time"><span class="loading-content"></span></div>\n      <div class="event__cell event__participant event__participant_home"><span class="loading-content"></span></div>\n      <div class="event__cell event__score"><span class="loading-content"></span></div>\n      <div class="event__cell event__participant event__participant_away event__participant_win"><span class="loading-content"></span></div>\n      <div class="event__cell event__periods"><span class="loading-content"></span></div>\n    </a>';
                    a += "</div></div>"
                }
                return a
            }
            a(".events-data").on("change", (function () {
                a(".middle-right .review").remove();
                var e = a(".events"),
                    t = a(".events-data-action").val(),
                    i = {
                        action: a(".events-data-action").val(),
                        date: a(".events-data-date").val(),
                        country: a(".events-data-country").length ? a(".events-data-country").val() : null,
                        tournament: a(".events-data-tournament").length ? a(".events-data-tournament").val() : null
                    };
                e.find(".spoiler-events").length ? (e.find(".spoiler__title").each((function () {
                    a(this).html('<span class="loading-content" style="width:' + a(this).width() + 'px;"></span>')
                })), e.find(".event__cell").each((function () {
                    a(this).html('<span class="loading-content"></span>')
                }))) : e.html(function () {
                    for (var a = "", e = 0; e < 5; e++) {
                        a += '<div class="spoiler spoiler-events open">\n        <div class="spoiler__header">\n          <div class="spoiler__title">\n            <span class="loading-content" style="width:160px;"></span>\n          </div>\n        </div>\n        <div class="spoiler__body">';
                        for (var t = 0; t < 4; t++) a += '<a class="event event-game" href="javascript:void(0)">\n          <div class="event__cell event__time"><span class="loading-content"></span></div>\n          <div class="event__cell event__participant event__participant_home"><span class="loading-content"></span></div>\n          <div class="event__cell event__score"><span class="loading-content"></span></div>\n          <div class="event__cell event__participant event__participant_away event__participant_win"><span class="loading-content"></span></div>\n          <div class="event__cell event__periods"><span class="loading-content"></span></div>\n        </a>';
                        a += "</div></div>"
                    }
                    return a
                }()), a.ajax({
                    data: JSON.stringify(i),
                    url: _APP.api + "/" + _APP.controller,
                    type: "POST",
                    dataType: "JSON",
                    success: function (a) {
                        try {
                            if (!a) return;
                            var i = "",
                                n = "",
                                s = !1;
                            a.forEach((function (a, e) {
                                var c = a.cT.toUpperCase() + ": " + a.tFt;
                                n != c && (s && (i += "</div></div>"), i += '<div class="spoiler spoiler-events', i += " open", i += '">\n              <div class="spoiler__header">', "games.team".indexOf(t) > -1 ? i += "" : "games.tournament".indexOf(t) > -1 ? i += '<a class="spoiler__title" href="'.concat(_APP[_APP.controller].url.root, "/").concat(a.cA, '" target="_blank">').concat(c, "</a>") : "games.country".indexOf(t) > -1 ? i += '<a class="spoiler__title" href="'.concat(_APP[_APP.controller].url.root, "/").concat(a.cA, "/").concat(a.tIDH, '" target="_blank"><img src="upload/images/').concat(_APP[_APP.controller].prefix, "t/").concat(_APP[_APP.controller].prefix, "t").concat(a.tIDH, '.png">').concat(c, "</a>") : i += '<a class="spoiler__title" href="'.concat(_APP[_APP.controller].url.root, "/").concat(a.cA, "/").concat(a.tIDH, '" target="_blank"><span class="flag flag-').concat(a.cID, '"></span>').concat(c, "</a>"), i += '</div>\n\n              <div class="spoiler__body">', s = !0), i += '<a class="event event-game" href="'.concat(_APP[_APP.controller].url.game, "/").concat(a.gIDH, '" target="_blank" data-idh="').concat(a.gIDH, '">\n              <div class="event__cell event__time">').concat(a.gSTt, '</div>\n              <div class="event__cell event__participant event__participant_home ').concat(a.hCR > a.aCR ? "event__participant_win" : "", '">\n                <span class="event__participant-title">').concat(a.hT, '</span>\n                <img class="event__participant-icon" src="upload/images/').concat(_APP[_APP.controller].prefix, "ha/").concat(_APP[_APP.controller].prefix, "ha").concat(a.hIDH, '.png">\n              </div>\n              <div class="event__cell event__score">\n                <div class="score">\n                  <div class="score__participant score__participant_home ').concat(a.hCR > a.aCR ? "score__participant_win" : "", '">').concat((a.hCR ? a.hCR:''), '</div>\n                  <div class="score__participant score__participant_away ').concat(a.aCR > a.hCR ? "score__participant_win" : "", '">').concat((a.aCR ? a.aCR : ''), '</div>\n                </div>\n              </div>\n              <div class="event__cell event__participant event__participant_away ').concat(a.hCR < a.aCR ? "event__participant_win" : "", '">\n                <span class="event__participant-title">').concat(a.aT, '</span>\n                <img class="event__participant-icon" src="upload/images/').concat(_APP[_APP.controller].prefix, "ha/").concat(_APP[_APP.controller].prefix, "ha").concat(a.aIDH, '.png">\n              </div>\n              <div class="event__cell event__periods">'), "football" == _APP.controller ? i += '<div class="score-period">'.concat(a.hRP1 ? a.hRP1 : 0, ":").concat(a.aRP1 ? a.aRP1 : 0, '</div><div class="score-period">').concat(a.hRP2 ? a.hRP2 : 0, ":").concat(a.aRP2 ? a.aRP2 : 0, "</div>") : "hockey" == _APP.controller && (a.hRP5 || a.aRP5 ? i += "Б&nbsp;" : (a.hRP4 || a.aRP4) && (i += "ОТ&nbsp;"), i += '<div class="score-period">'.concat(a.hRP1 ? a.hRP1 : 0, ":").concat(a.aRP1 ? a.aRP1 : 0, '</div><div class="score-period">').concat(a.hRP2 ? a.hRP2 : 0, ":").concat(a.aRP2 ? a.aRP2 : 0, '</div><div class="score-period">').concat(a.hRP3 ? a.hRP3 : 0, ":").concat(a.aRP3 ? a.aRP3 : 0, "</div>")), i += "</div>\n            </a>", n = c
                            })), i += "</div></div>", e.html(i)
                        } catch (a) {
                            console.log(a)
                        }
                    }
                })
            })), a(".review-data-idh").on("change", (function () {
                var e = this.value,
                    t = a(".middle-right");
                t.html(function (a, e, t) {
                    return '<div class="review fixed">\n      <div class="review-info"></div>\n      <div class="review-main">\n        <a class="review-main__participant review-participant review-participant_home" href="javascript:void(0)"">\n          <div class="review-participant__logo"><span class="loading-content"></span></div>\n          <div class="review-participant__name"><span class="loading-content"></span></div>\n        </a>\n        <div class="review-main__middle">\n          <div class="review-date"><span class="loading-content"></span></div>\n          <div class="review-time"><span class="loading-content"></span></div>\n          <div class="review-score score"><span class="loading-content"></span></div>\n          <div class="review-periods"><span class="loading-content"></div>\n          <div class="review-status"><span class="loading-content"></span></div>\n          <a class="review-btn" href="'.concat(_APP[_APP.controller].url.game, "/").concat(a, '">Перейти на страницу матча</a>\n        </div>\n        <a class="review-main__participant review-participant review-participant_away" href="javascript:void(0)">\n          <div class="review-participant__logo"><span class="loading-content"></span></div>\n          <div class="review-participant__name"><span class="loading-content"></span></div>\n        </a>\n      </div>\n      <div class="review-nav">\n        <div class="nav nav-review">\n          <a class="nav__tab btn js-tab active" href="javascript:void(0)" data-subnav="livecentre">Live Centre</a>\n          <a class="nav__tab btn js-tab" href="javascript:void(0)" data-subnav="h2h">H2H</a>\n          <a class="nav__tab btn js-tab" href="javascript:void(0)" data-target="#game-series" onclick="document.querySelector(\'.review-data-action\').changeValue(\'game.series\')">Серии</a>\n        </div>\n      </div>\n      <div class="review-subnav active">\n        <div class="review-subnav__item nav nav-livecentre active">\n          <a class="nav__tab btn-link js-tab active" href="javascript:void(0)" data-target="#game-detail" onclick="document.querySelector(\'.review-data-action\').changeValue(\'game.detail\')"><span>Обзор матча</span></a>\n          <a class="nav__tab btn-link js-tab" href="javascript:void(0)" data-target="#game-statistic" onclick="document.querySelector(\'.review-data-action\').changeValue(\'game.statistic\')"><span>Статистика</span></a>\n          <a class="nav__tab btn-link js-tab" href="javascript:void(0)" data-target="#game-lineups" onclick="document.querySelector(\'.review-data-action\').changeValue(\'game.lineups\')"><span>Составы</span></a>\n        </div>\n        <div class="review-subnav__item nav nav-statistic">\n          <a class="nav__tab btn-link" href="javascript:void(0)"><span><span class="loading-content"></span></span></a>\n          <a class="nav__tab btn-link" href="javascript:void(0)"><span><span class="loading-content"></span></span></a>\n          <a class="nav__tab btn-link" href="javascript:void(0)"><span><span class="loading-content"></span></span></a>\n        </div>\n        <div class="review-subnav__item nav nav-h2h">\n          <a class="nav__tab btn-link js-tab active" href="javascript:void(0)" data-target="#game-h2h-all" onclick="document.querySelector(\'.review-data-action\').changeValue(\'game.h2h.all\')"><span>Итого</span></a>\n          <a class="nav__tab btn-link js-tab" href="javascript:void(0)" data-target="#game-h2h-home" onclick="document.querySelector(\'.review-data-action\').changeValue(\'game.h2h.home\')"><span><span class="js-participant-name_home"><?=$post[\'hT\']?></span> дома</span></a>\n          <a class="nav__tab btn-link js-tab" href="javascript:void(0)" data-target="#game-h2h-away" onclick="document.querySelector(\'.review-data-action\').changeValue(\'game.h2h.away\')"><span><span class="js-participant-name_away"><?=$post[\'aT\']?></span> в гостях</span></a>\n        </div>\n      </div>\n      <div class="review-contents">\n        <div id="game-detail" class="review-content detail active loaded">') + function () {
                        for (var a = "", e = '<div class="detail-event">\n      <div class="detail-event__cell detail-event__time"><span class="loading-content"></span></div>\n      <div class="detail-event__cell detail-event__icon"><span class="loading-content"></span></div>\n      <div class="detail-event__cell detail-event__player"><span class="loading-content"></span></div>\n    </div>', t = '<div class="detail-card__header">\n      <div class="detail-card__cell detail-card__time"><img class="icon icon-clock" src="images/icons/icon-clock-gray.svg"></div>\n      <div class="detail-card__cell detail-card__icon"><img class="icon icon-whistle" src="images/icons/icon-whistle-gray.svg"></div>\n      <div class="detail-card__cell detail-card__player"><img class="icon icon-person" src="images/icons/icon-person-gray.svg"></div>\n    </div>\n    <div class="detail-card__body">'.concat(e).concat(e, "</div>"), i = 1; i <= _APP[_APP.controller].numberPeriods; i++) a += '<div class="detail-period">\n        <div class="detail-period__title">'.concat(i, " ").concat(_T[_APP.controller].period, '</div>\n        <div class="detail-period__participants">\n          <div class="detail-period__participant detail-period__participant_home">\n            <div class="detail-card detail-card_small">').concat(t, '</div>\n          </div>\n          <div class="detail-period__participant detail-period__participant_away">\n            <div class="detail-card detail-card_small">').concat(t, "</div>\n          </div>\n        </div>\n      </div>");
                        return a
                    }() + '</div>\n        <div id="game-statistic" class="review-content statistic">' + function () {
                        for (var a = '<div class="nav">\n      <a class="nav__tab btn-link" href="javascript:void(0)"><span><span class="loading-content"></span></span></a>\n      <a class="nav__tab btn-link" href="javascript:void(0)"><span><span class="loading-content"></span></span></a>\n      <a class="nav__tab btn-link" href="javascript:void(0)"><span><span class="loading-content"></span></span></a>\n    </div>\n    <div class="statistic-contents">\n      <div class="statistic-content active">', e = 0; e < 14; e++) a += '<div class="statistic-row">\n          <div class="statistic-text-group"></div>\n          <div class="statistic-bar-group">\n            <div class="statistic-bar statistic-bar--home"><span class="loading-content"></span></div>\n              <div class="statistic-bar statistic-bar--away"><span class="loading-content"></span></div>\n            </div>\n          </div>';
                        return a += "</div>\n    </div>"
                    }() + '</div>\n        <div id="game-lineups" class="review-content lineups">' + function () {
                        for (var a = "", e = 0; e < 10; e++) a += '<tr><td class="summary-vertical fl"><span class="loading-content"></span></td><td class="summary-vertical fr"><span class="loading-content"></span></td></tr>';
                        return '<div class="lineups-header">\n      <div class="lineups-header__participant lineups-header__participant_home"><span class="loading-content"></span></div>\n      <div class="lineups-header__title"><span class="loading-content"></span></div>\n      <div class="lineups-header__participant lineups-header__participant_away"><span class="loading-content"></span></div>\n    </div>\n    <table class="lineups-table">\n      <tbody>\n        <tr><td colspan="2" class="h-part"><span class="loading-content"></span></td></tr>\n         '.concat(a, '\n        <tr><td colspan="2" class="h-part"><span class="loading-content"></span></td></tr>\n        ').concat(a, "\n      </tbody>\n    </table>")
                    }() + '</div>\n        <div id="game-h2h-all" class="review-content h2h">' + h() + '</div>\n        <div id="game-h2h-home" class="review-content h2h">' + h() + '</div>\n        <div id="game-h2h-away" class="review-content h2h">' + h() + '</div>\n        <div id="game-series" class="review-content series"></div>\n      </div>\n    </div>'
                }(e)), t.find(".review-nav .js-tab").on("click", (function () {
                    var e = this.dataset.subnav,
                        t = this.dataset.target;
                    e ? "livecentre" == e ? (a(".review-subnav").addClass("active"), a(".nav-livecentre").siblings().removeClass("active"), a(".nav-livecentre").addClass("active"), a(".nav-livecentre .nav__tab.active").length ? a(".nav-livecentre .nav__tab.active").first().trigger("click") : a(".nav-livecentre .nav__tab").first().trigger("click")) : "h2h" == e && (a(".review-subnav").addClass("active"), a(".nav-h2h").siblings().removeClass("active"), a(".nav-h2h").addClass("active"), a(".nav-h2h .nav__tab.active").length ? a(".nav-h2h .nav__tab.active").first().trigger("click") : a(".nav-h2h .nav__tab").first().trigger("click")) : t && "#game-series" == t && (a(".review-subnav").removeClass("active"), a(".review-subnav__item").removeClass("active"))
                }));
                var n = {
                    action: "game",
                    idh: e
                };
                a.ajax({
                    data: JSON.stringify(n),
                    url: _APP.api + "/" + _APP.controller,
                    type: "POST",
                    dataType: "JSON",
                    success: function (e) {
                        try {
                            if (!e) return;
                            a(".review-data-st").val(e.game.ST), a(".review-data-hidh").val(e.game.HIDH), a(".review-data-aidh").val(e.game.AIDH), a(".review-data-ht").val(e.game.HT), a(".review-data-at").val(e.game.AT), t.find(".review-info").text(e.game.info), t.find(".review-participant_home").attr("href", _APP[_APP.controller].url.team + "/" + e.game.HIDH), t.find(".review-participant_away").attr("href", _APP[_APP.controller].url.team + "/" + e.game.AIDH), t.find(".review-participant_home .review-participant__logo").html('<img class="review-participant__image" src="upload/images/'.concat(_APP[_APP.controller].prefix, "ha/").concat(_APP[_APP.controller].prefix, "ha").concat(e.game.HIDH, '.png">')), t.find(".review-participant_away .review-participant__logo").html('<img class="review-participant__image" src="upload/images/'.concat(_APP[_APP.controller].prefix, "ha/").concat(_APP[_APP.controller].prefix, "ha").concat(e.game.AIDH, '.png">')), t.find(".review-participant_home .review-participant__name").text(e.game.HT), t.find(".review-participant_away .review-participant__name").text(e.game.AT), t.find(".review-date").text(i.a.unix(e.game.ST).format("DD.MM.YYYY")), t.find(".review-time").text(i.a.unix(e.game.ST).format("hh:mm")), t.find(".review-score").html('<div class="review-score__participant review-score__participant_home">'.concat((e.game.hCR ? e.game.hCR : ''), '</div><div class="review-score__participant review-score__participant_away">').concat((e.game.aCR ? e.game.aCR : ''), "</div>")), "football" == _APP.controller ? t.find(".review-periods").html('<div class="review-periods__item">'.concat(e.game.hRP1 ? e.game.hRP1 : 0, ":").concat(e.game.aRP1 ? e.game.aRP1 : 0, '</div><div class="review-periods__item">').concat(e.game.hRP2 ? e.game.hRP2 : 0, ":").concat(e.game.aRP2 ? e.game.aRP2 : 0, "</div>")) : "hockey" == _APP.controller && t.find(".review-periods").html('<div class="review-periods__item">'.concat(e.game.hRP1 ? e.game.hRP1 : 0, ":").concat(e.game.aRP1 ? e.game.aRP1 : 0, '</div><div class="review-periods__item">').concat(e.game.hRP2 ? e.game.hRP2 : 0, ":").concat(e.game.aRP2 ? e.game.aRP2 : 0, '</div><div class="review-periods__item">').concat(e.game.hRP3 ? e.game.hRP3 : 0, ":").concat(e.game.aRP3 ? e.game.aRP3 : 0, "</div>")), t.find(".review-status").text(_T[_APP.controller].status[e.game.SID]), t.find("#game-detail").html(v(e.detail)), a(".js-participant-name_home").text(e.game.HT), a(".js-participant-name_away").text(e.game.AT)
                        } catch (a) {
                            console.log(a)
                        }
                    }
                })
            })), a(".review-nav").length && a(".review-nav .js-tab").on("click", (function () {
                var e = this.dataset.subnav,
                    t = this.dataset.target;
                e ? "h2h" == e && (a(".review-subnav").addClass("active"), a(".nav-h2h").siblings().removeClass("active"), a(".nav-h2h").addClass("active"), a(".nav-h2h .nav__tab.active").length ? a(".nav-h2h .nav__tab.active").first().trigger("click") : a(".nav-h2h .nav__tab").first().trigger("click")) : t && ("#game-detail" == t || "#game-series" == t || "#game-statistic" == t || "#game-lineups" == t) && (a(".review-subnav").removeClass("active"), a(".review-subnav__item").removeClass("active"))
            })), a(".review-data-action").on("change", (function () {
                var e = this.value,
                    t = a("#" + e.replace(/\./gim, "-"));
                if (!t.hasClass("loaded"))
                    if ("game.detail" == e) {
                        var s = {
                            action: e,
                            idh: a(".review-data-idh").val()
                        };
                        a.ajax({
                            data: JSON.stringify(s),
                            url: _APP.api + "/" + _APP.controller,
                            type: "POST",
                            dataType: "JSON",
                            success: function (a) {
                                try {
                                    if (!a) return;
                                    t.html(v(a)), t.addClass(["loaded", "active"])
                                } catch (a) {
                                    t.empty(), console.log(a)
                                }
                            },
                            error: function () {
                                t.empty()
                            }
                        })
                    } else if ("game.statistic" == e) {
                    var c = {
                        action: e,
                        idh: a(".review-data-idh").val()
                    };
                    a.ajax({
                        data: JSON.stringify(c),
                        url: _APP.api + "/" + _APP.controller,
                        type: "POST",
                        dataType: "JSON",
                        success: function (a) {
                            try {
                                if (!a) return;
                                t.html(p(a)), t.find(".nav-statistic .nav__tab").first().addClass("active"), t.find(".statistic-content").first().addClass("active"), t.addClass(["loaded", "active"])
                            } catch (a) {
                                t.empty(), console.log(a)
                            }
                        },
                        error: function () {
                            t.empty()
                        }
                    })
                } else if ("game.lineups" == e) {
                    var l = {
                        action: e,
                        idh: a(".review-data-idh").val()
                    };
                    a.ajax({
                        data: JSON.stringify(l),
                        url: _APP.api + "/" + _APP.controller,
                        type: "POST",
                        dataType: "JSON",
                        success: function (a) {
                            try {
                                if (!a) return;
                                t.html(_(a)), t.addClass(["loaded", "active"])
                            } catch (a) {
                                t.empty(), console.log(a)
                            }
                        },
                        error: function () {
                            t.empty()
                        }
                    })
                } else if (["game.h2h.all", "game.h2h.home", "game.h2h.away"].indexOf(e) > -1) {
                    var r = e.substr(e.lastIndexOf(".") + 1),
                        o = {
                            action: e,
                            st: a(".review-data-st").val(),
                            idh: a(".review-data-idh").val(),
                            hidh: a(".review-data-hidh").val(),
                            aidh: a(".review-data-aidh").val()
                        };
                    a.ajax({
                        data: JSON.stringify(o),
                        url: _APP.api + "/" + _APP.controller,
                        type: "POST",
                        dataType: "JSON",
                        success: function (e) {
                            try {
                                if (!e) return;
                                t.html(function (e, t) {
                                    var n = a(".review-data-hidh").val(),
                                        s = a(".review-data-aidh").val(),
                                        c = a(".review-data-ht").val(),
                                        l = a(".review-data-at").val(),
                                        r = "";
                                    return e.forEach((function (a, e) {
                                        var o, d;
                                        a.data.length && ("all" == t ? 0 == e ? (o = "spoiler-h2h-h", d = c) : 1 == e ? (o = "spoiler-h2h-a", d = l) : 2 == e && (o = "spoiler-h2h-ha", d = c + " - " + l) : "home" == t ? 0 == e ? (o = "spoiler-h2h-h", d = c) : 1 == e && (o = "spoiler-h2h-ha", d = c + " - " + l) : "away" == t && (0 == e ? (o = "spoiler-h2h-a", d = l) : 1 == e && (o = "spoiler-h2h-ha", d = c + " - " + l)), r += '<div class="spoiler spoiler-h2h '.concat(o, ' open">\n        <div class="spoiler__header">\n          <span class="spoiler__title">Последние игры: ').concat(d, '</span>\n        </div>\n        <div class="spoiler__body">'), a.data.forEach((function (a) {
                                            var c = "",
                                                l = "";
                                            "all" == t ? 0 == e ? n == a.hIDH ? a.hCR == a.aCR ? c = "draw" : (a.hRP1 == a.aRP1 && (l = "p1draw"), a.hCR > a.aCR ? c = "win" : a.hCR < a.aCR && (c = "lose")) : n == a.aIDH && (a.hCR == a.aCR ? c = "draw" : (a.hRP1 == a.aRP1 && (l = "p1draw"), a.aCR > a.hCR ? c = "win" : a.aCR < a.hCR && (c = "lose"))) : 1 == e && (s == a.hIDH ? a.hCR == a.aCR ? c = "draw" : (a.hRP1 == a.aRP1 && (l = "p1draw"), a.hCR > a.aCR ? c = "win" : a.hCR < a.aCR && (c = "lose")) : s == a.aIDH && (a.hCR == a.aCR ? c = "draw" : (a.hRP1 == a.aRP1 && (l = "p1draw"), a.aCR > a.hCR ? c = "win" : a.aCR < a.hCR && (c = "lose")))) : "home" == t ? 0 == e && (n == a.hIDH ? a.hCR == a.aCR ? c = "draw" : (a.hRP1 == a.aRP1 && (l = "p1draw"), a.hCR > a.aCR ? c = "win" : a.hCR < a.aCR && (c = "lose")) : n == a.aIDH && (a.hCR == a.aCR ? c = "draw" : (a.hRP1 == a.aRP1 && (l = "p1draw"), a.aCR > a.hCR ? c = "win" : a.aCR < a.hCR && (c = "lose")))) : "away" == t && 0 == e && (s == a.hIDH ? a.hCR == a.aCR ? c = "draw" : (a.hRP1 == a.aRP1 && (l = "p1draw"), a.hCR > a.aCR ? c = "win" : a.hCR < a.aCR && (c = "lose")) : s == a.aIDH && (a.hCR == a.aCR ? c = "draw" : (a.hRP1 == a.aRP1 && (l = "p1draw"), a.aCR > a.hCR ? c = "win" : a.aCR < a.hCR && (c = "lose"))));
                                            var o = "";
                                            "win" == c ? o = "В" : "lose" == c ? o = "П" : "draw" == c && (o = "Н");
                                            var d = i.a.unix(a.gST);
                                            r += '<a class="event event-game event-h2h" href="'.concat(_APP[_APP.controller].url.game, "/").concat(a.gIDH, '" target="_blank">\n            <div class="event__cell event__time">').concat(d.format("DD.MM.YY"), '</div>\n            <div class="event__cell event__participant event__participant_home'), a.hCR > a.aCR && (r += " event__participant_win"), "all" == t ? (0 == e && n == a.hIDH && (r += " event__participant_current"), 1 == e && s == a.hIDH && (r += " event__participant_current")) : "home" == t ? 0 == e && n == a.hIDH && (r += " event__participant_current") : "away" == t && 0 == e && s == a.hIDH && (r += " event__participant_current"), r += '">\n              <span class="event__participant-title">'.concat(a.hT, '</span>\n              <img class="event__participant-icon" src="upload/images/').concat(_APP[_APP.controller].prefix, "ha/").concat(_APP[_APP.controller].prefix, "ha").concat(a.hIDH, '.png">\n            </div>\n            <div class="event__cell m-event__score m-event__score_').concat(c, " m-event__score_").concat(l, '"><div class="score">').concat(o, '</div></div>\n            <div class="event__cell event__score event__score_').concat(c, " event__score_").concat('">\n              <div class="score">\n                <div class="score__participant score__participant_home ').concat(a.hCR > a.aCR ? "score__participant_win" : "", '">').concat((a.hCR ? a.hCR:''), '</div>\n                <div class="score__participant score__participant_away ').concat(a.aCR > a.hCR ? "score__participant_win" : "", '">').concat((a.aCR ? a.aCR:''), '</div>\n              </div>\n            </div>\n            <div class="event__cell event__participant event__participant_away'), a.aCR > a.hCR && (r += " event__participant_win"), "all" == t ? (0 == e && n == a.aIDH && (r += " event__participant_current"), 1 == e && s == a.aIDH && (r += " event__participant_current")) : "home" == t ? 0 == e && n == a.aIDH && (r += " event__participant_current") : "away" == t && 0 == e && s == a.aIDH && (r += " event__participant_current"), r += '">\n              <span class="event__participant-title">'.concat(a.aT, '</span>\n              <img class="event__participant-icon" src="upload/images/').concat(_APP[_APP.controller].prefix, "ha/").concat(_APP[_APP.controller].prefix, "ha").concat(a.aIDH, '.png">\n            </div>\n            <div class="event__cell event__periods">'), "football" == _APP.controller ? r += '<div class="score-period">'.concat(a.hRP1 ? a.hRP1 : 0, ":").concat(a.aRP1 ? a.aRP1 : 0, '</div><div class="score-period">').concat(a.hRP2 ? a.hRP2 : 0, ":").concat(a.aRP2 ? a.aRP2 : 0, "</div>") : "hockey" == _APP.controller && (a.hRP5 || a.aRP5 ? r += "Б&nbsp;" : (a.hRP4 || a.aRP4) && (r += "ОТ&nbsp;"), r += '<div class="score-period">'.concat(a.hRP1 ? a.hRP1 : 0, ":").concat(a.aRP1 ? a.aRP1 : 0, '</div><div class="score-period">').concat(a.hRP2 ? a.hRP2 : 0, ":").concat(a.aRP2 ? a.aRP2 : 0, '</div><div class="score-period">').concat(a.hRP3 ? a.hRP3 : 0, ":").concat(a.aRP3 ? a.aRP3 : 0, "</div>")), r += "</div>\n          </a>"
                                        })), r += "</div>", a.count > a.data.length && (r += '<div class="spoiler-h2h__more"><a class="spoiler-h2h__more-link js-h2h-more" href="javascript:void(0)" data-target="#game-h2h-'.concat(t, '" data-section="'), "all" == t ? 0 == e ? r += "h" : 1 == e ? r += "a" : 2 == e && (r += "ha") : "home" == t ? (0 == e && (r += "h"), 1 == e && (r += "ha")) : "away" == t && (0 == e && (r += "a"), 1 == e && (r += "ha")), r += '">Показать больше матчей</a></div>'), r += "</div>")
                                    })), r
                                }(e, r)), t.attr("data-count", e.count), t.find(".spoiler-h2h-h .event-game").slice(0, 5).addClass("show"), t.find(".spoiler-h2h-a .event-game").slice(0, 5).addClass("show"), t.find(".spoiler-h2h-ha .event-game").slice(0, 5).addClass("show"), t.find(".js-h2h-more").on("click", d), t.addClass(["loaded", "active"])
                            } catch (a) {
                                t.empty(), console.log(a)
                            }
                        },
                        error: function () {
                            t.empty()
                        }
                    })
                } else if ("game.series" == e) {
                    var h = {
                        action: e,
                        idh: a(".review-data-idh").val()
                    };
                    a.ajax({
                        data: JSON.stringify(h),
                        url: _APP.api + "/" + _APP.controller,
                        type: "POST",
                        dataType: "JSON",
                        success: function (e) {
                            try {
                                if (!e) return;
                                t.html(function (e) {
                                    var t = a(".review-data-hidh").val(),
                                        i = a(".review-data-aidh").val(),
                                        s = a(".review-data-ht").val(),
                                        c = a(".review-data-at").val(),
                                        l = "",
                                        r = "",
                                        o = "",
                                        d = "";
                                    _APP.scheme[_APP.controller].series.forEach((function (a) {
                                        e["H" + a] && e["H" + a] > 2 && (l += '<div class="series-item">' + _T[_APP.controller].series[a].replace("{team}", s).replace("{game}", '<span class="series-item__count">' + e["H" + a] + "</span> " + Object(n.a)(e["H" + a], ["матч", "матча", "матчей"])) + "</div>"), e["HH" + a] && e["HH" + a] > 2 && (r += '<div class="series-item">' + _T[_APP.controller].series[a].replace("{team}", s).replace("{game}", '<span class="series-item__count">' + e["HH" + a] + "</span> " + Object(n.a)(e["HH" + a], ["матч", "матча", "матчей"])) + "</div>"), e["A" + a] && e["A" + a] > 2 && (o += '<div class="series-item">' + _T[_APP.controller].series[a].replace("{team}", c).replace("{game}", '<span class="series-item__count">' + e["A" + a] + "</span> " + Object(n.a)(e["A" + a], ["матч", "матча", "матчей"])) + "</div>"), e["AA" + a] && e["AA" + a] > 2 && (d += '<div class="series-item">' + _T[_APP.controller].series[a].replace("{team}", c).replace("{game}", '<span class="series-item__count">' + e["AA" + a] + "</span> " + Object(n.a)(e["AA" + a], ["матч", "матча", "матчей"])) + "</div>")
                                    }));
                                    var v = "";
                                    l.length && (v += '<div class="spoiler spoiler-series open">\n      <div class="spoiler__header">\n        <span class="spoiler__title">\n          <img class="spoiler__title-icon" src="upload/images/'.concat(_APP[_APP.controller].prefix, "ha/").concat(_APP[_APP.controller].prefix, "ha").concat(t, '.png">\n          ').concat(s, '\n        </span>\n      </div>\n      <div class="spoiler__body">').concat(l, "</div>\n    </div>"));
                                    r.length && (v += '<div class="spoiler spoiler-series open">\n      <div class="spoiler__header">\n        <span class="spoiler__title">\n          <img class="spoiler__title-icon" src="upload/images/'.concat(_APP[_APP.controller].prefix, "ha/").concat(_APP[_APP.controller].prefix, "ha").concat(t, '.png">\n          ').concat(s, ' дома\n        </span>\n      </div>\n      <div class="spoiler__body">').concat(r, "</div>\n    </div>"));
                                    o.length && (v += '<div class="spoiler spoiler-series open">\n      <div class="spoiler__header">\n        <span class="spoiler__title">\n          <img class="spoiler__title-icon" src="upload/images/'.concat(_APP[_APP.controller].prefix, "ha/").concat(_APP[_APP.controller].prefix, "ha").concat(i, '.png">\n          ').concat(c, '\n        </span>\n      </div>\n      <div class="spoiler__body">').concat(o, "</div>\n    </div>"));
                                    d.length && (v += '<div class="spoiler spoiler-series open">\n      <div class="spoiler__header">\n        <span class="spoiler__title">\n          <img class="spoiler__title-icon" src="upload/images/'.concat(_APP[_APP.controller].prefix, "ha/").concat(_APP[_APP.controller].prefix, "ha").concat(i, '.png">\n          ').concat(c, ' в гостях\n        </span>\n      </div>\n      <div class="spoiler__body">').concat(d, "</div>\n    </div>"));
                                    return v
                                }(e)), t.addClass("loaded")
                            } catch (a) {
                                t.empty(), console.log(a)
                            }
                        },
                        error: function () {
                            t.empty()
                        }
                    })
                }
            })), a(".mr-review-data-action").on("change", (function () {
                var e = this.value,
                    t = a("#" + e.replace(/\./gim, "-"));
                if (!t.hasClass("loaded"))
                    if ("game.statistic" == e) {
                        var i = {
                            action: e,
                            idh: a(".review-data-idh").val()
                        };
                        a.ajax({
                            data: JSON.stringify(i),
                            url: _APP.api + "/" + _APP.controller,
                            type: "POST",
                            dataType: "JSON",
                            success: function (a) {
                                try {
                                    if (!a) return;
                                    t.html(p(a, "mr-"));
                                    var e = $statistic.find(".mr-nav-statistic .nav__tab").first();
                                    e.addClass("active"), $statistic.find(e.attr("data-target")).addClass(["loaded", "active"])
                                } catch (a) {
                                    t.empty(), console.log(a)
                                }
                            },
                            error: function () {
                                t.empty()
                            }
                        })
                    } else if ("game.lineups" == e) {
                    var n = {
                        action: e,
                        idh: a(".review-data-idh").val()
                    };
                    a.ajax({
                        data: JSON.stringify(n),
                        url: _APP.api + "/" + _APP.controller,
                        type: "POST",
                        dataType: "JSON",
                        success: function (a) {
                            try {
                                if (!a) return;
                                t.html(_(a));
                                var e = $lineups.find(".mr-nav-lineups .nav__tab").first();
                                e.addClass("active"), $lineups.find(e.attr("data-target")).addClass(["loaded", "active"])
                            } catch (a) {
                                t.empty(), console.log(a)
                            }
                        },
                        error: function () {
                            t.empty()
                        }
                    })
                }
            }))
        }).call(this, t(1))
    },
    154: function (a, e, t) {
        var i = {
            "./af": 6,
            "./af.js": 6,
            "./ar": 7,
            "./ar-dz": 8,
            "./ar-dz.js": 8,
            "./ar-kw": 9,
            "./ar-kw.js": 9,
            "./ar-ly": 10,
            "./ar-ly.js": 10,
            "./ar-ma": 11,
            "./ar-ma.js": 11,
            "./ar-sa": 12,
            "./ar-sa.js": 12,
            "./ar-tn": 13,
            "./ar-tn.js": 13,
            "./ar.js": 7,
            "./az": 14,
            "./az.js": 14,
            "./be": 15,
            "./be.js": 15,
            "./bg": 16,
            "./bg.js": 16,
            "./bm": 17,
            "./bm.js": 17,
            "./bn": 18,
            "./bn-bd": 19,
            "./bn-bd.js": 19,
            "./bn.js": 18,
            "./bo": 20,
            "./bo.js": 20,
            "./br": 21,
            "./br.js": 21,
            "./bs": 22,
            "./bs.js": 22,
            "./ca": 23,
            "./ca.js": 23,
            "./cs": 24,
            "./cs.js": 24,
            "./cv": 25,
            "./cv.js": 25,
            "./cy": 26,
            "./cy.js": 26,
            "./da": 27,
            "./da.js": 27,
            "./de": 28,
            "./de-at": 29,
            "./de-at.js": 29,
            "./de-ch": 30,
            "./de-ch.js": 30,
            "./de.js": 28,
            "./dv": 31,
            "./dv.js": 31,
            "./el": 32,
            "./el.js": 32,
            "./en-au": 33,
            "./en-au.js": 33,
            "./en-ca": 34,
            "./en-ca.js": 34,
            "./en-gb": 35,
            "./en-gb.js": 35,
            "./en-ie": 36,
            "./en-ie.js": 36,
            "./en-il": 37,
            "./en-il.js": 37,
            "./en-in": 38,
            "./en-in.js": 38,
            "./en-nz": 39,
            "./en-nz.js": 39,
            "./en-sg": 40,
            "./en-sg.js": 40,
            "./eo": 41,
            "./eo.js": 41,
            "./es": 42,
            "./es-do": 43,
            "./es-do.js": 43,
            "./es-mx": 44,
            "./es-mx.js": 44,
            "./es-us": 45,
            "./es-us.js": 45,
            "./es.js": 42,
            "./et": 46,
            "./et.js": 46,
            "./eu": 47,
            "./eu.js": 47,
            "./fa": 48,
            "./fa.js": 48,
            "./fi": 49,
            "./fi.js": 49,
            "./fil": 50,
            "./fil.js": 50,
            "./fo": 51,
            "./fo.js": 51,
            "./fr": 52,
            "./fr-ca": 53,
            "./fr-ca.js": 53,
            "./fr-ch": 54,
            "./fr-ch.js": 54,
            "./fr.js": 52,
            "./fy": 55,
            "./fy.js": 55,
            "./ga": 56,
            "./ga.js": 56,
            "./gd": 57,
            "./gd.js": 57,
            "./gl": 58,
            "./gl.js": 58,
            "./gom-deva": 59,
            "./gom-deva.js": 59,
            "./gom-latn": 60,
            "./gom-latn.js": 60,
            "./gu": 61,
            "./gu.js": 61,
            "./he": 62,
            "./he.js": 62,
            "./hi": 63,
            "./hi.js": 63,
            "./hr": 64,
            "./hr.js": 64,
            "./hu": 65,
            "./hu.js": 65,
            "./hy-am": 66,
            "./hy-am.js": 66,
            "./id": 67,
            "./id.js": 67,
            "./is": 68,
            "./is.js": 68,
            "./it": 69,
            "./it-ch": 70,
            "./it-ch.js": 70,
            "./it.js": 69,
            "./ja": 71,
            "./ja.js": 71,
            "./jv": 72,
            "./jv.js": 72,
            "./ka": 73,
            "./ka.js": 73,
            "./kk": 74,
            "./kk.js": 74,
            "./km": 75,
            "./km.js": 75,
            "./kn": 76,
            "./kn.js": 76,
            "./ko": 77,
            "./ko.js": 77,
            "./ku": 78,
            "./ku.js": 78,
            "./ky": 79,
            "./ky.js": 79,
            "./lb": 80,
            "./lb.js": 80,
            "./lo": 81,
            "./lo.js": 81,
            "./lt": 82,
            "./lt.js": 82,
            "./lv": 83,
            "./lv.js": 83,
            "./me": 84,
            "./me.js": 84,
            "./mi": 85,
            "./mi.js": 85,
            "./mk": 86,
            "./mk.js": 86,
            "./ml": 87,
            "./ml.js": 87,
            "./mn": 88,
            "./mn.js": 88,
            "./mr": 89,
            "./mr.js": 89,
            "./ms": 90,
            "./ms-my": 91,
            "./ms-my.js": 91,
            "./ms.js": 90,
            "./mt": 92,
            "./mt.js": 92,
            "./my": 93,
            "./my.js": 93,
            "./nb": 94,
            "./nb.js": 94,
            "./ne": 95,
            "./ne.js": 95,
            "./nl": 96,
            "./nl-be": 97,
            "./nl-be.js": 97,
            "./nl.js": 96,
            "./nn": 98,
            "./nn.js": 98,
            "./oc-lnc": 99,
            "./oc-lnc.js": 99,
            "./pa-in": 100,
            "./pa-in.js": 100,
            "./pl": 101,
            "./pl.js": 101,
            "./pt": 102,
            "./pt-br": 103,
            "./pt-br.js": 103,
            "./pt.js": 102,
            "./ro": 104,
            "./ro.js": 104,
            "./ru": 105,
            "./ru.js": 105,
            "./sd": 106,
            "./sd.js": 106,
            "./se": 107,
            "./se.js": 107,
            "./si": 108,
            "./si.js": 108,
            "./sk": 109,
            "./sk.js": 109,
            "./sl": 110,
            "./sl.js": 110,
            "./sq": 111,
            "./sq.js": 111,
            "./sr": 112,
            "./sr-cyrl": 113,
            "./sr-cyrl.js": 113,
            "./sr.js": 112,
            "./ss": 114,
            "./ss.js": 114,
            "./sv": 115,
            "./sv.js": 115,
            "./sw": 116,
            "./sw.js": 116,
            "./ta": 117,
            "./ta.js": 117,
            "./te": 118,
            "./te.js": 118,
            "./tet": 119,
            "./tet.js": 119,
            "./tg": 120,
            "./tg.js": 120,
            "./th": 121,
            "./th.js": 121,
            "./tk": 122,
            "./tk.js": 122,
            "./tl-ph": 123,
            "./tl-ph.js": 123,
            "./tlh": 124,
            "./tlh.js": 124,
            "./tr": 125,
            "./tr.js": 125,
            "./tzl": 126,
            "./tzl.js": 126,
            "./tzm": 127,
            "./tzm-latn": 128,
            "./tzm-latn.js": 128,
            "./tzm.js": 127,
            "./ug-cn": 129,
            "./ug-cn.js": 129,
            "./uk": 130,
            "./uk.js": 130,
            "./ur": 131,
            "./ur.js": 131,
            "./uz": 132,
            "./uz-latn": 133,
            "./uz-latn.js": 133,
            "./uz.js": 132,
            "./vi": 134,
            "./vi.js": 134,
            "./x-pseudo": 135,
            "./x-pseudo.js": 135,
            "./yo": 136,
            "./yo.js": 136,
            "./zh-cn": 137,
            "./zh-cn.js": 137,
            "./zh-hk": 138,
            "./zh-hk.js": 138,
            "./zh-mo": 139,
            "./zh-mo.js": 139,
            "./zh-tw": 140,
            "./zh-tw.js": 140
        };

        function n(a) {
            var e = s(a);
            return t(e)
        }

        function s(a) {
            if (!t.o(i, a)) {
                var e = new Error("Cannot find module '" + a + "'");
                throw e.code = "MODULE_NOT_FOUND", e
            }
            return i[a]
        }
        n.keys = function () {
            return Object.keys(i)
        }, n.resolve = s, a.exports = n, n.id = 154
    },
    2: function (a, e, t) {
        "use strict";

        function i(a, e) {
            return (a = Math.abs(a) % 100) >= 5 && a <= 20 ? e[2] : 1 == (a %= 10) ? e[0] : a >= 2 && a <= 4 ? e[1] : e[2]
        }
        t.d(e, "a", (function () {
            return i
        }))
    }
});

$('.icon-soccer-ball-own').parent().parent().append('<div class="detail-event__desc">(Автогол)</div>');