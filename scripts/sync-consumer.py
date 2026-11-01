#!/usr/bin/env python3
"""Copy the versioned shared source into a product and record its provenance."""
from pathlib import Path
import hashlib,json,shutil,subprocess,sys
source=Path(__file__).resolve().parents[1]
product=Path(sys.argv[1]).resolve()
if not (product/'package.json').is_file(): raise SystemExit('Not a product repository')
target=product/'vendor/lingxi-core'
files=[p for base in ['src','crates'] for p in (source/base).rglob('*') if p.is_file() and 'target' not in p.parts]
files += [source/'LICENSE',source/'package.json']
target.mkdir(parents=True,exist_ok=True)
for path in files:
 dest=target/path.relative_to(source);dest.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(path,dest)
commit=subprocess.check_output(['git','rev-parse','HEAD'],cwd=source,text=True).strip()
manifest={'repository':'https://github.com/Cyber-bike1949/LingXiCore','commit':commit,'files':{str(p.relative_to(source)):hashlib.sha256(p.read_bytes()).hexdigest() for p in files}}
(target/'SOURCE.json').write_text(json.dumps(manifest,indent=2)+'\n')
print('Updated',target,'from',commit)
