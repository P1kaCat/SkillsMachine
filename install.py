"""Install bundled skills without overwriting existing installations."""
import argparse, os, pathlib, shutil

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--dest', type=pathlib.Path, default=pathlib.Path(os.environ.get('CODEX_HOME', str(pathlib.Path.home()/'.codex'))) / 'skills')
    parser.add_argument('--only', nargs='+', help='Install only the named skills')
    parser.add_argument('--list', action='store_true')
    parser.add_argument('--dry-run', action='store_true')
    args = parser.parse_args()
    source = pathlib.Path(__file__).resolve().parent / 'skills'
    skills = {p.name:p for p in source.iterdir() if p.is_dir() and (p/'SKILL.md').is_file()}
    if args.list:
        print('\n'.join(sorted(skills))); print(f'Total: {len(skills)}'); return
    selected = sorted(args.only or skills)
    unknown = set(selected) - skills.keys()
    if unknown: parser.error('Unknown skills: '+', '.join(sorted(unknown)))
    destination = args.dest.expanduser().resolve()
    if destination == source.resolve() or source.resolve() in destination.parents:
        parser.error('Destination must be outside the bundled skills directory')
    installed = skipped = 0
    for name in selected:
        folder = skills[name]
        if any(p.is_symlink() for p in [folder, *folder.rglob('*')]):
            parser.error('Symbolic links are not accepted: '+name)
        target = destination / name
        if target.exists() or target.is_symlink():
            print('SKIP '+name+' (already exists)'); skipped += 1; continue
        if not args.dry_run:
            destination.mkdir(parents=True, exist_ok=True)
            shutil.copytree(folder, target, ignore=shutil.ignore_patterns('__pycache__','*.pyc'))
        installed += 1
    print(f'{"Would install" if args.dry_run else "Installed"}: {installed}; skipped: {skipped}; destination: {destination}')

if __name__ == '__main__': main()
